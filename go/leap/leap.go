package leap

const testVersion = 2

// IsLeapYear function testing whether a give year is a leap year
func IsLeapYear(year int) bool {
	if year % 400 == 0 {
		return true
	} else if (year % 4 == 0) && (year % 100 != 0) {
		return true
	} else {
		return false
	}
}
