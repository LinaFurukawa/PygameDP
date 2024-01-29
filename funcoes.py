def colisao_entre_retangulos(r1_x,r1_y,r1_w,r1_h,r2_x,r2_y,r2_w,r2_h):
    if r1_x < r2_x + r2_w and r1_x + r1_w > r2_x and r1_y < r2_y + r2_h and r1_y + r1_h > r2_y:
        return True
    else:
        return False