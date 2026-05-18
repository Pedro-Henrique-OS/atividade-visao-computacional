import cv2

# Carrega a imagem
imagem = cv2.imread(r"C:\Users\pedro\Documents\IA\exercicio2\foto.jpg")

# Aplica o filtro gaussiano
suavizada = cv2.GaussianBlur(imagem, (15, 15), 0)

# Salva a nova imagem
cv2.imwrite("resultado.jpg", suavizada)

# Mensagem final
print("Filtro Gaussiano aplicado com sucesso!")