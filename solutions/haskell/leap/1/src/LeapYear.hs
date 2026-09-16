module LeapYear (isLeapYear) where
import GHC.IO.Encoding.Failure (CodingFailureMode(TransliterateCodingFailure))

isLeapYear :: Integer -> Bool
isLeapYear year 
  | year `rem` 4 == 0 && year `rem` 100 /= 0 = True
  | year `rem` 400 == 0 && year `rem` 100 == 0 = True
  | otherwise = False
  

  
