from year_2015.day_2.main import calculate_ribbon_ft, calculate_wrapping_paper_sq_ft


class TestWrappingPaper:
    def test_unique_dimensions(self):
        assert calculate_wrapping_paper_sq_ft("2x3x4") == 58

    def test_repeated_dimensions(self):
        assert calculate_wrapping_paper_sq_ft("1x1x10") == 43


class TestRibbon:
    def test_unique_dimensions(self):
        assert calculate_ribbon_ft("2x3x4") == 34

    def test_repeated_dimensions(self):
        assert calculate_ribbon_ft("1x1x10") == 14
