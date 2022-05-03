
--Funcao statistics 
--Ira retorna o primeiro caractere da string com '.' e o tamanho da string 
statistics :: String -> (String , Int)
statistics palavras = ([head palavras , '.' , last palavras],length palavras)
--Funcao main 
main = do
palavras <- readLn
print $ statistics palavras
--Printa a funcao