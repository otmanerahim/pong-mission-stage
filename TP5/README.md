# TP5 - Craig Reynolds - Comportement de poursuite

Ce TP est destiné à tous les étudiants qui souhaitent en savoir plus sur d'autres techniques utilisés pour implémenter des IA intelligentes dans les jeux vidéos, sur ce TP j'ai envie de vous faire découvrir les algorithmes d'un informaticien du nom de Craig Reynolds, il est aujourd'hui célèbre pour ses différents algorithmes dit "réactifs" où les IA sont des **agents autonomes**, ses travaux sur les IA sont aujourd'hui utilisés dans de nombreux jeux vidéos ! [Ce lien](https://www.red3d.com/cwr/steer/) sont les résultats de ses recherches c'est intéressant d'y jeter un coup d'oeil !

Dans ce TP vous allez implémenter un des algorithmes de Craig Reynolds, qui est le **comportement de poursuite**, vous vous posez sûrement la question de à quoi cela sert puisque notre IA qu'on a créée suit la balle sans problème ! Et bien je vous dirais oui ! Mais nous allons voir une autre manière intelligente d'implémenter un tel comportement, Si on reprend les recherches de Craig reynolds, on peut voir qu'il voulait que ses agents autonomes se rapproche le plus d'un être vivant qui aurait une perception sur le monde qui l'entoure, **"the ability to navigate around their world in a life-like and improvisational manner"**.

Voici ci-dessous un exemple de plusieurs agents autonomes utilisant des comportements diverses de Craig reynolds, comme le comportement de fuite, plutôt impressionant non ?

![](https://repository-images.githubusercontent.com/258305543/28971980-92d2-11ea-8a66-4d0d91c0e790)

Si vous ne comprenez pas , pas de panique je vais essayer de synthétiser un maximim l'essentiel de son travail.

## Agent autonome

Un agent autonome fait référence à une entité qui dispose d’une connaissance propre à propos de ce qui l’entoure et une capacité qui lui permet de se mouvoir et prendre des décisions de son propre chef. La première question à se poser avant d’implémenter les comportements est de savoir comment peut-on un agent autonome peut être représentable, et quel type d’agent autonome nous voulons représentés. Comme nous souhaitons implémenter un des comportements proposés par Craig Reynolds, j’ai repris ses recherches décrivant un agent autonome.

## Vehicle

Lorsque Craig Reynolds a publié son travail, il a utilisé le mot “véhicule” pour décrire un agent autonome. Un véhicule sert ici à englober une large gamme de moyen de transport (un avion, un bateau, une voiture, un cheval,etc…) .
Il s’est inspiré des travaux de Valentino Braitenberg, un neuro-scientifique et cybernéticien décrivant des véhicules mécaniques (hypothétiques) très simples manifestant des comportements tels que la peur, l’agression, l’amour, la prévoyance ou encore l’optimisme. A partir de ses travaux, Craig Reynolds a imaginé un véhicule “idéalisé” pour décrire ses comportements. Le mot idéalisé a été choisi car Craig Reynolds ne se soucie par réellement de l’ingénierie réelle de tels véhicules, il voulait simplement un modèle de véhicule très simpliste pouvant répondre aux règles qu’il a établi.

### Force

Avant de décrire le modèle du véhicule et d’aller plus loin dans les explications, il est important de comprendre ce que signifie une force, tous les calculs qui seront décrits par la suite font appel à cette notion fondamentale en physique. On rappelle que l’on veut simuler un véhicule, les mouvements du véhicule doivent se rapprocher de la réalité. La définition de la force vient du célèbre scientifique britannique Isaac Newton. “A force is a vector that causes an object with mass to accelerate.” Ainsi chaque force exercée sur le véhicule sera décrit par un vecteur, et chaque force aura un impact sur la vitesse du véhicule.

### Modèle du véhicule

Le modèle du véhicule est défini par cinq paramètres :
• la masse : une valeur scalaire
• la position : un vecteur
• la vélocité du véhicule : un vecteur
• la vitesse maximale : une valeur scalaire
• la vitesse de changement de direction maximale : une valeur scalaire

Le véhicule a une masse, une position ainsi qu’une vitesse nommée vélocité qui au cours du temps peut changer car la vitesse du véhicule dépend des forces qui sont appliquées dessus. En plus de cela le véhicule a une vitesse maximale qu’il ne peut dépasser et également une vitesse de changement de direction limitée.

Bien maintenant que tout cela est compris il est temps de passé la création de notre modèle de raquette !

## Modèle de notre raquette

- masse
- position
- vélocité
- vitesse maximum

Pour notre modèle on ne prendra pas la vitesse de changement de direction du véhicule car notre raquette se déplace uniquement sur l'axe y il n'y a pas de rotation possible.

## Comportement de poursuite

Notre modèle aura pour comportement un comportement de poursuite, afin de comprendre comment cela marche on va revenir sur un cas plus général.

C’est ici un des concepts les plus importants à comprendre si on reprend le modèle de véhicule, on a un véhicule avec une simple force de vélocité.

![](/ressources/TP6/craig_1.png)

On voit ici qu’il faut un autre vecteur pour que notre véhicule puisse atteindre son but, on pourrait très bien ajouter un autre vecteur force qui attire le véhicule et calculer cette force, mais selon Craig Reynolds notre véhicule doit être plus intelligent que cela. On veut que notre véhicule puisse faire la décision de tourner vers la cible par rapport à sa vitesse actuelle et sa direction.

Plus précisément, le véhicule va devoir choisir sa direction pour se déplacer, c’est la force désirée par le véhicule appelée “desired velocity", ensuite cette force va être comparée avec sa vitesse actuelle ("current velocity"), puis une force va être appliquée en fonction de ces deux paramètres.

la formule pour calculer cette force est décrite par la formule établi par Craig Reynolds :

“steering force = desired velocity - current velocity”

![](/ressources/TP6/craig_2.png)

## Cas pour la raquette

Dans le cas de notre raquette la formule sera la même !

```py
def seek(self, ball_pos):
        steer = np.zeros(2)
        # On calcul le vecteur désirée
        desired = ...
        # On normalise le vecteur
        if np.linalg.norm(desired) > 0:
            desired = desired/np.linalg.norm(desired)
            # On restreint le vecteur si celle-ci dépasse la vitesse max autorisée
            desired = ...
            # On calcule la force nécessaire en reprenant la formule de craig reynolds
            steer = ...
            # On limite le vecteur force
            if np.linalg.norm(steer) > self.maxforce:
                steer = self.normalizeto(steer, self.maxforce)
        return steer

    def apply_craig_behavior(self, ball_pos,can_react):
        if(can_react):
            self.position = np.array((int(self.posX), int(self.posY)), dtype=float)
            # get new velocity
            self.velocity += self.acceleration

            # Limit velocity to max speed
            if np.linalg.norm(self.velocity) > self.maxvelocity:
                self.velocity = self.normalizeto(self.velocity, self.maxvelocity)
            self.position += self.velocity
            self.acceleration *= 0

            # On calcule la force
            correction_force = (self.seek(ball_pos))
            # Puis on l'applique à notre raquette
            self.applyForce(correction_force)

            self.move()

    def move(self):
        self.posY = self.position[1]

    def applyForce(self, force):
        self.acceleration += force

    def normalizeto(self, vector, max):
        if np.linalg.norm(vector) > 0:
            return (vector/np.linalg.norm(vector)) * max
        else:
            return np.zeros(2)
```

Les trois dernières fonctions sont données pour vous aider à compléter l'algorithme !

Et voilà les TPS sont terminés, je vous ai montré une autre manière d'implémenter une IA en utilisant des notions de physiques qui se rapproche plus de notre monde réel :) Vous pouvez aller plus loin en regardant d'autres comportements qui sont tout aussi intéressants ! Et pourquoi pas implémenter le comportement de fuite de craig reynolds dans les TPs pacman !
