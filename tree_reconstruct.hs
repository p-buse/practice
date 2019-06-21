
date Tree a = Nil | Tree a (Tree a) (Tree a)
  deriving Show

reconstruct :: Eq a => [a] -> [a] -> Tree a
reconstruct (preRoot : preLR) inorder = Tree preRoot treeL treeR
  where
    (inL, inRoot : inR) = break (==preRoot) inorder
    (preL, preR) = splitAt (lenght inL) preLR
    treeL = reconstruct preL inL
    treeR = reconstruct preR inR
reconstruct [] _ = Nil


