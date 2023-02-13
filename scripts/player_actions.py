from bge import logic , events 







def getMouseAngleY( cont , own , sen_mouse_movement , act_mouse_y ):


    if sen_mouse_movement.positive:
        cont.activate( act_mouse_y ) 
        own["MOUSE_Y_ANGLE"] = -act_mouse_y.angle[1] + 90



    pass


def setMouseAngleAction(cont , own):
    mouse   = logic.mouse.events
    tc      = logic.keyboard.events
    keys    = tc[events.WKEY] or tc[events.SKEY] or tc[events.AKEY] or tc[events.DKEY] 

    #--------------------------------
    

    if mouse[events.RIGHTMOUSE]:
        own.playAction( "Player_Bracos_Mirando" , 1 , 1 , layer = 2 )
        own.playAction( "Player_Torso_Mirando" , own["MOUSE_Y_ANGLE"] , own["MOUSE_Y_ANGLE"] , layer = 3 )

        if keys:
            own.playAction( "Player_WALK._pernas" , 1 , 32 , layer = 4 )
            

    elif keys:
        own.playAction( "Player_WALK" , 1 , 32 , layer = 1 )

    else:
        own.playAction( "Player_IDLE" , 1 , 148 , layer = 2 )


    pass



def playerMovente(cont , own):
    mouse   = logic.mouse.events
    tc      = logic.keyboard.events
    keys    = tc[events.WKEY] or tc[events.SKEY] or tc[events.AKEY] or tc[events.DKEY] 

    #--------------------------------

    if tc[events.WKEY]:
        own.applyMovement([ 0 , -0.080 , 0 ] , True )
        
    
    pass



def start(cont):
    own = cont.owner


    print("TUDO OK")



def update(cont):
    own = cont.owner

    #-----------------------
    MouseMovement = cont.sensors["MouseMovement"]


    #---------------------------
    MouseY = cont.actuators["MouseY"]

    #--------------------------

    playerMovente(cont , own)

    getMouseAngleY( cont , own , 
                    sen_mouse_movement  = MouseMovement, 
                    act_mouse_y         = MouseY
                    )

    setMouseAngleAction(cont , own)