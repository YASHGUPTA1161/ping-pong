# detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

# detect l_paddle misses
    if ball.xcor() > -380:
        ball.reset_position()