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



-- make me a default foldr with type signature to ge tthe length of a list
-- find the length of a list using foldr
foldr' :: (Num a, Int b) => (a -> b -> b) -> b -> [a] -> b
                        -- function        start  list   output
def (Num: val1, Int:val2) 

lengthOfList :: [a] -> Int
lengthOfList xs = foldr (\_ acc -> acc + 1) 0 xs
(lambda: x = x + 1)
lengthOfList xs = foldr (incrementFunction) 0 xs where
        incrementFunction x = incrementFunction + 1
[5, 6, 7, 8]

[1, 2, 3]
3 : 2 : 1 : []
3 + 2 + 1 + 0

-- lets have some fun with some lists
-- we dont have a for operator in haskell, so we use recursion

-- incrementListWithRecursion :: [Int] -> [Int]
-- incrementListWithRecursion [] = []
-- incrementListWithRecursion (x:xs) = incrementWithRecursion xs : [x+1]
-- incrementListWithRecursion lst = incrementWithRecursion (tail lst) : [head lst]
inc (start:restOfList)

incrementListWithMapping :: [Int] -> [Int]
incrementListWithMapping xs = map (+1) xs

incrementListWithComprehension :: [Int] -> [Int]
incrementListWithComprehension xs = [x+1 | x <- xs]



filteringList :: [Int] -> [Int]
filteringList xs = filter (<4) xs
[1..10]

-- todo in lesson, have a function which doubles any number thats odd

--passing functions in as parameters
myMap :: (Int -> Int) -> [Int] -> [Int]
myMap func list = map func list


shiftChar :: Int -> Char -> Char
shiftChar i c = chr((mod(((ord c) - 97) + i) 26) + 97)

caesarShift :: String -> Int -> String
caesarShift xs i = map (shiftChar i) xs

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
            A = val left tree right tree
            a = node (2 tree (node 1) tree (node) 3)


insert :: Ord a => a -> Tree a -> Tree a
insert x Empty = Node x Empty Empty
insert x Tree

insert (x:xs)
insert list

insert x (Node y left right)
    | x <= y    = Node y (insert x left) right
    | otherwise = Node y left (insert x right)


{--
the . operator composes 2 functions together, i.e. map and filter to combine 
    into 1 function which takes in a list
the $ operator is used to basically say, bracket everything past this point

--}

-- here is a function which doubles every number bigger than 3
result xs = map (*2) (filter (>3) xs)

-- so we can get rid of the last pair of brackets using the $ operator
result2 xs = map (*2) $ filter (>3) xs

-- and using the . operator, we compose map (*2) and filter (>3) into its own function, then pass [1..10] into that using the $ operator
result3 xs = map (*2) . filter (>3) $ xs

result3 -> (result3) xs



map (*2) . filter (>3)

-- heres a cool interaction with currying
result4 :: (Num a, Ord a) => [a] -> [a]
result4 = map (*2) . filter (>3)
f(g(x))
f . g x
{--
how curring functions work
say we have a function add x y
functions in haskell can only take one parameter and return 1 value
so how do we take in the 2 parameters for add x y
well the function descriptor for add is:
add :: (Num a) => a -> a -> a
add x y
add (add x) y
under the hood, this calls (add y (add x))
--}

-- how to define functions inside other functions
filterWhere :: (Num a, Ord a) => [a] -> [a]
filterWhere xs = filter fn xs where
    fn x = 
        let y = 3 in
        x > y

        (\x -> x > 3)
filterLambda :: (Num a, Ord a) => [a] -> [a]
filterLambda xs = filter (\x -> x > 3) xs

1 2 3 4 5

