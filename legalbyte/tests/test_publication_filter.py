# Import the business rule that locates an exclusion criterion.
from apps.requests.services import find_exclusion_criterion

def test_finds_criterion_ignoring_case_and_accents():

    # The publication intentionally uses uppercase text without accents.
    publication = "AVISO DE PREGAO ELETRONICO PARA CONTRATACAO"

    # Criteria preserve the form originally provided by the user.
    criteria = ["Ineditoriais", "Pregão eletrônico"]

    # Execute the business rule without HTTP, database, or spreadsheet access.
    result = find_exclusion_criterion(publication, criteria)

    # Return the original criterion so it can be written to the output file.
    assert result == "Pregão eletrônico"

def test_does_not_treat_solicitacao_as_licitacao():
    # "Solicitação" contais the character sequence "licitação",
    # but it must not trigger the exclusion criterion.
    publication = "O Advogado apresentou uma solicitação ao juízo."

    criteria = ["Licitação"]

    result = find_exclusion_criterion(publication, criteria)

    # No exclusion should be found.
    assert result is None

def test_finds_licitacao_as_independent_word():
    # "Licitação" appears as an independent word and must be detected.
    publication = "Foi publicaçãdo um aviso de licitação para contratação."

    criteria = ["Licitação"]

    result = find_exclusion_criterion(publication, criteria)

    assert result == "Licitação"

def test_returns_last_matching_criterion_when_criteria_overlap():
    # Both criteria match, but the later and more specific criterion
    # must be returned to preserve the legaxy behavior.
    publication = "O comando do Exército publicou um novo ato."

    criteria = [
        "Exército",
        "Comando do exército",
    ]

    result = find_exclusion_criterion(publication, criteria)

    assert result == "Comando do exército"

def test_finds_licitacao_when_followed_by_text_without_separator():

    # Some legacy publications concatenate "licitação" with other text.
    publication = "AVISO DE LICITAÇÃOMUNHOZ2022"

    criteria = ["Licitação"]

    result = find_exclusion_criterion(publication, criteria)

    assert result == "Licitação"