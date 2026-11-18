# BytesIO represents a binary file stored only in memory.
from io import BytesIO

# Workbook creates an XLSX file and load_workbook reads one.
from openpyxl import Workbook, load_workbook

# Import the spreadsheet processing service that will be implemented.
from apps.requests.services import process_publications_spreadsheet

def test_processes_treated_sheet_and_adds_analysis_columns():

    # Create an input workbook entirely in memory.
    input_workbook = Workbook()

    # The legacy contract requires a sheet named TRATADAS.
    input_sheet = input_workbook.active
    input_sheet.title = "PUBLICAÇÕES"

    # Add the columns expected in the input spreadsheet.
    input_sheet.append([
        "Nº do Processo",
        "Data de Cadastro",
        "Data de Disponibilização",
        "Data de Publicação",
        "Publicação",
    ])

    # This row contains only "solicitação" and must remain relevant.
    input_sheet.append([
        "0001",
        "01/01/2026",
        "02/01/2026",
        "03/01/2026",
        "O advogado apresentou uma solicitação ao juízo.",
    ])

    # This row contains an exclusion criterion.
    input_sheet.append([
        "0002",
        "01/01/2026",
        "02/01/2026",
        "03/01/2026",
        "Foi publicado um aviso de PREGAO ELETRONICO.",
    ])

    # Save the input workbook into an in-memory binary file.
    input_file = BytesIO()
    input_workbook.save(input_file)

    # Return the file cursor to the beginning before reading it.
    input_file.seek(0)

    criteria = ["Licitação", "Pregão eletrônico"]

    # Process the input and receive another in-memory XLSX file.
    output_file = process_publications_spreadsheet(
        input_file,
        criteria,
        sheet_name="PUBLICAÇÕES",
    )

    # Open the generated workbook to verify its contents.
    output_workbook = load_workbook(output_file)
    output_sheet = output_workbook.active

    # Convert the worksheet rows into values that are easy to assert.
    rows = list(output_sheet.iter_rows(values_only=True))

    # The output must preserve the input columns and add two analysis columns.
    assert rows[0] == (
        "Nº do Processo",
        "Data de Cadastro",
        "Data de Disponibilização",
        "Data de Publicação",
        "Publicação",
        "Retorno robô",
        "Critério localizado",
    )

    # "Solicitação" alone must not trigger the "Licitação" criterion.
    assert rows[1][-2:] == ("OK", None)
    
    # The matching criterion must mark the publication for exclusion.
    assert rows[2][-2:] == (
        "Desconsiderar publicação",
        "Pregão eletrônico",
    )

def test_marks_row_without_publication_as_ok():
    # Create a workbook with a row whose publication is empty.
    input_workbook = Workbook()
    input_sheet = input_workbook.active
    input_sheet.title = "PUBLICAÇÕES"

    input_sheet.append([
        "Nº do Processo",
        "Publicação",
    ])

    input_sheet.append([
        "0001",
        None,
    ])

    input_file = BytesIO()
    input_workbook.save(input_file)
    input_file.seek(0)
    input_workbook.close()

    output_file = process_publications_spreadsheet(
        input_file,
        criteria=["Licitação"],
        sheet_name="PUBLICAÇÕES",
    )

    output_workbook = load_workbook(output_file)
    output_sheet = output_workbook.active
    rows = list(output_sheet.iter_rows(values_only=True))

    # The row must remain and be classified as relevant.
    assert rows[1] == (
        "0001",
        None,
        "OK",
        None,
    )

    output_workbook.close()
    output_file.close()
    input_file.close()