# set key repeat rate
xset r rate 180 60

redshift -l 51.50336630:-0.1276250 &

# load .Xresources
xrdb ~/.Xresources

# init window manager
# (nwm, i3)
exec i3
