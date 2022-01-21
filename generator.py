from PIL import Image
import os


def maker(background_index, body_index, eye_index, mouth_index, ornament_index, final_file_number):
    background = Image.open(f"backgrounds/background_{background_index}.png")
    body = Image.open(f"bodies/body_{body_index}.png")
    eye = Image.open(f"eyes/eyes_{eye_index}.png")
    mouth = Image.open(f"mouth/mouth_{mouth_index}.png")
    ornament = Image.open(f"ornaments/ornament_{ornament_index}.png")

    body_trans = Image.new("RGBA", background.size)
    body_trans.paste(body, mask=body)
    Image.alpha_composite(
        background, body_trans).save("images/final.png")

    final = Image.open("images/final.png")
    eye_trans = Image.new("RGBA", final.size)
    eye_trans.paste(eye, (420, 440), mask=eye,)
    Image.alpha_composite(
        final, eye_trans).save("images/final_a.png")
    os.remove("images/final.png")

    final = Image.open("images/final_a.png")
    mouth_trans = Image.new("RGBA", final.size)
    mouth_trans.paste(mouth, (455, 580), mask=mouth,)
    Image.alpha_composite(
        final, mouth_trans).save("images/final_b.png")
    os.remove("images/final_a.png")

    '''
    final = Image.open("images/final_b.png")
    ornament_trans = Image.new("RGBA", final.size)
    ornament_trans.paste(ornament, (455, 20), mask=ornament,)
    Image.alpha_composite(
        final, ornament_trans).save(f"images/final{final_file_number}.png")
    os.remove("images/final_b.png")
    '''


maker(5, 4, 1, 3, 2, 69)
