// Bibliotecas padrao
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include "hDrv_~name~.h"
/*
#include "drv_i2c.h"
#include "~NAME~_~PORTNAME~.h"
*/


/*
TAG: lDrvFunctionsPrototypes
MODEL{
~returnType~        port_~name~_~fnName~_~portname~ (hdrv_~name~_h handler ~argsWithTipes~);
}
*/



const ldrv_~name~_port_t ~PORTNAME~_~NAME~_DRIVER = 
{
/*
TAG: lDrvPortInitialization
MODEL{
    .~fnName~      = port_~name~_~fnName~_~portname~,
}
*/
};
const ldrv_~name~_port_t *~PORTNAME~_~NAME~_DRIVER_HANDLER = &~PORTNAME~_~NAME~_DRIVER;


typedef struct ~PORTNAME~_instance_
{
    // Instance variables
}~PORTNAME~_instance_t;



//====================================================================
// Internal functions
//====================================================================


//====================================================================
// External functions by ~PORTNAME~_RCT_DRIVER
//====================================================================

void* port_~name~_init_~portname~ (~PORTNAME~_init_args_t args)
{
    ~PORTNAME~_instance_t* this = handler;
    handler = malloc(sizeof(~PORTNAME~_init_args_t));

    // TODO: Init instance here!

    return(handler);
}

/*
TAG: ldrvPublicFunctions
MODEL{
~returnType~        port_~name~_~fnName~_~portname~ (hdrv_~name~_h handler ~argsWithTipes~)
{
    assert(handler != NULL);
    ~PORTNAME~_instance_t* this = handler;

    // TODO: Insert yout code here!
}
}
*/