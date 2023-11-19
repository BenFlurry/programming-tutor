import Data.Char
-- this is how you comment btw


-- if conditions
ifCondition :: Bool -> Bool -> String
ifCondition condition anothercondition = 
    if condition then "condition is true"
    else if anothercondition then "another condition is true"
    else "none of the conditions are true"

-- here we can use guard conditions 
guardIfCondition :: Bool -> Bool -> String
guardIfCondition condition anothercondition 
    | condition = "condition is true"
    | anothercondition = "another condition is true"
    | otherwise = "none of the conditions are true"

caseCondition :: Bool -> Bool -> String
caseCondition condition anotherCondition = 
    case (condition, anotherCondition) of 
        (True, _) -> "condition is true"
        (_, True) -> "another conidition is true"
        otherwise -> "none of the coniditions are true"

-- lets have some fun with some lists
-- we dont have a for operator in haskell, so we use recursion

incrementListWithRecursion :: [Int] -> [Int]
incrementListWithRecursion [] = []
incrementListWithRecursion (x:xs) = (x+1) : incrementListWithRecursion xs

incrementListWithMapping :: [Int] -> [Int]
incrementListWithMapping xs = map (+1) xs

incrementListWithComprehension :: [Int] -> [Int]
incrementListWithComprehension lst = [x+1 | x <- lst]

filteringList :: [Int] -> [Int]
filteringList xs = filter (<4) xs

-- todo in lesson, have a function which doubles any number thats odd

--passing functions in as parameters
myMap :: (a -> a) -> [a] -> [a]
myMap func list = map func list

shiftChar :: Int -> Char -> Char
shiftChar i c = chr((mod(((ord c) - 97) + i) 26) + 97)

caesarShift :: String -> Int -> [Char]
caesarShift xs i = map (shiftChar i) xs

{--
how curring functions work
say we have a function add x y
functions in haskell can only take one parameter and return 1 value
so how do we take in the 2 parameters for add x y
well the function descriptor for add is:
add :: (Num a) => a -> a -> a
add x y
under the hood, this calls add y (add x)
--}

{--
Haskell is a strongly typed language, meaning that.
Eq: this type can be checked with another variable for equality (==, !=)
Ord (inherits Eq): this type can be ordered (<, <=, >)
Show: this type can be printed
Num: the representation of all number types
Integral (inherits Num): the representation of all non-decimal number
Fractional (inherits Num): the representation of all fractional numbers (supports / and recip)
Floating (inherits Fractional): the representation of all decimal numbers (supports trigonomectic functions)
Int (inherits Integral): 32 or 64 bit integer, fixed size
Integer (inherits Integral): unbounded size integer
Float (inherits Floating): 32 bit float (3-6 d.p)
Double (inherits FLoating): 64 bit float (15-17 d.p)
--}

-- heres how you define your own datatypes
data Tree a = Empty | Node a (Tree a) (Tree a) deriving (Show, Eq)

insert :: Ord a => a -> Tree a -> Tree a
insert x Empty = Node x Empty Empty
insert x (Node y left right)
    | x <= y    = Node y (insert x left) right
    | otherwise = Node y left (insert x right)

{--
the . operator composes 2 functions together, i.e. map and filter to combine into 1 function which takes in a list
the $ operator is used to basically say, bracket everything past this point

--}

-- here is a function which doubles every number bigger than 3
let result = map (*2) (filter (>3) [1..10])

-- so we can get rid of the last pair of brackets using the $ operator
let result2 = map (*2) $ filter (>3) [1..10]

-- and using the . operator, we compose map (*2) and filter (>3) into its own function, then pass [1..10] into that using the $ operator
let result3 = map (*2) . filter (>3) $ [1..10]


    
