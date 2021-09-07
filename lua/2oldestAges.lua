-- The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

-- The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

local t = {}
function t.twoOldestAges(ages)
  local oldests = {0, 0}
  for i = 1, #ages do
    if ages[i] > oldests[2] then
      oldests[2] = ages[i]
    elseif ages[i] > oldests[1]
      then oldests[1] = ages[i]
    end
  end
  
  return oldests
end
return t
