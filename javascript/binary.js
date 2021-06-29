function decimalToBase(number, base) {
  let remainder = number
  let result = []
  let shouldDivide = true

  while (shouldDivide) {
    result[result.length] = remainder % base
    remainder = Math.floor(remainder / base)

    if (remainder < base) {
      result[result.length] = remainder
      shouldDivide = false
    }
  }

  return result.reverse().join('')
}
