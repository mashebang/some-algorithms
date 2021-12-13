function rgb(r, g, b) {
  const toRGB = (x) => {
    if (x < 0) return '00'
    if (x > 255) return 'FF'
    const hex = x.toString(16).toUpperCase()
    return hex.length > 1 ? hex : `0${hex}`
  }
  return `${toRGB(r)}${toRGB(g)}${toRGB(b)}`
}
