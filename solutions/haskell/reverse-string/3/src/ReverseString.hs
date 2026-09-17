module ReverseString (reverseString) where

reverseString :: String -> String
reverseString [] = []
reverseString str = doReverseString str []


doReverseString :: [a] -> [a] -> [a]
doReverseString [] result = result
doReverseString (hd : tl) result = doReverseString tl (hd : result)
