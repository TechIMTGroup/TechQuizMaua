from PIL import Image, ImageTk


def loadImage(path, resize=None):
    if resize != None:
        return ImageTk.PhotoImage(Image.open(path).resize(resize))
    else:
        return ImageTk.PhotoImage(Image.open(path))


def ImageLogo(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\LOGO.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\LOGO.png")


def ImageInformation(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\Information.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\Information.png")


def ImageCheckEdit(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\check.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\check.png")


def ImageEdit(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\EDIT.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\EDIT.png")


def ImageRnkgLogo(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\RANKING.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\RANKING.png")


def ImageLogoNEscrita(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\LogoSemEscrita.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\LogoSemEscrita.png")

def ImageCardQuiz(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\CardQuiz.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\CardQuiz.png")

def ImageGoBack(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\Back.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\Back.png")
    
def ImageGoFoward(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\Foward.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\Foward.png")
    
def ImageQuestao(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\questao.png", resize)
    else:
        return loadImage("TechQuiz\Imagens\questao.png")
    
def ImageLupa(resize=None):
    if resize != None:
        return loadImage("TechQuiz\Imagens\lupa.PNG", resize)
    else:
        return loadImage("TechQuiz\Imagens\lupa.PNG")
    