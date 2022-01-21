from PIL import Image
import os


def maker(background_index, body_index, eye_index, mouth_index, ornament_index):
    background = Image.open(f"backgrounds/background_{background_index}.png")
    body = Image.open(f"bodies/body_{body_index}.png")
    eye = Image.open(f"eyes/eyes_{eye_index}.png")
    mouth = Image.open(f"mouth/mouth_{mouth_index}.png")
    ornament = Image.open(f"ornaments/ornament_{ornament_index}.png")

    box = (0, 0)
    body_trans = Image.new("RGBA", background.size)
    body_trans.paste(body, box, mask=body)
    Image.alpha_composite(
        background, body_trans).save("images/final.png")

    final = Image.open("images/final.png")
    eye_trans = Image.new("RGBA", final.size)
    eye_trans.paste(eye, box, mask=eye)
    Image.alpha_composite(
        final, eye_trans).save("images/final2.png")
    os.remove("images/final.png")

    '''
    final = Image.open("images/final.png")
    eyes_trans = Image.new("RGBA", final.size)
    eyes_trans.paste(eye, box, mask=body)
    Image.alpha_composite(background, body_trans).save("images/final.png")
    '''


'''
FUNCTION WHICH PASTES TRANSPERENT IMAGES, HERE FOR FUTURE REFERENCE
def trans_paste():
    box = (0, 0)
    background = Image.open(f"backgrounds/background_1.png")
    body = Image.open(f"bodies/body_2.png")
    body_trans = Image.new("RGBA", background.size)
    body_trans.paste(body, box, mask=body)
    new_img = Image.alpha_composite(
        background, body_trans).save("images/final.png")
'''


maker(5, 3, 1, 1, 1)


# trans_paste()
