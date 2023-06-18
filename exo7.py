# Exercice 7 : 
# Créer des classes de base avec les classmethod 
# Notions abordées: les classes, les méthodes. On continue avec
# classe Voiture, pour laquelle nous allons maintenant créer des 'classmethod'.
# Cela nous permettra donc de définir une marque, un prix et une couleur par
# défaut pour 2 types de voitures de luxe : une Lamborghini et une Porsche. Nous
# allons donc à partir de ces deux classmethod créer deux instances de voitures :
# 1. >>> Lamborghini = Voiture.lamborghini() 2. >>> print(lamborghini.prix) 3.
# 150000 4. >>> porsche = Voiture.porsche() 5. >>> print(porsche.prix) 6. 200000
# La Lamborghini devra avoir comme marque "Lamborghini", comme prix 150,000€ et
# comme couleur "rouge". La porsche quant à elle devra avoir comme
# marque "Porsche", comme prix 200,000€ et comme couleur "noire". Le code devra
# afficher : La Lamborghini a pour marque : Lamborghini, prix : 150.000€ et
# couleur : rouge La Porsche a pour marque : Porsche, prix : 200.000€ et couleur :
# noire Astuces : Pour créer une classmethod, il faut utiliser le
# décorateur @classmethod. 