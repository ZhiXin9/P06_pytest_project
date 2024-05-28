from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 5555
        b = 1111
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 4444
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 10
        b = 10
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 100
        assert result == expected

    def test_divide(self):
        # arrange
        a = 428
        b = 4
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 107
        assert result == expected

    def test_divide_by_zero(self):
        # Arrange
        cal = Calculator()
        
        # Act / Assert
        try:
            cal.divide(10, 0)
        except ZeroDivisionError:
            # Assert
            assert True  # ZeroDivisionError should be raised
