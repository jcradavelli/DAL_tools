// Bibliotecas padrao
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

// Arquivo de driver publico
#include "hDrv_~name~.h"


// L drivers
/*
TAG: lDriversCfiles
MODEL{
#if USE_~PORTNAME~ == true
#include "PORT/~PORTNAME~/lDrv_~name~.c"
#endif
}
*/

typedef struct hdrv_~name~_
{
    void*               pvHandler;
    const ldrv_~name~_port_t *port;
}hdrv_~name~_t;

// Funções de uso interno
static hdrv_~name~_t* __get_context (hdrv_~name~_h handler)
{
    assert (handler != NULL);
    hdrv_~name~_t* this = handler;
    return(this);
}

hdrv_~name~_h hdrv_~name~_init (const hdrv_~name~_initArgs_t args)
{
    hdrv_~name~_t *~name~ = malloc(sizeof(hdrv_~name~_initArgs_t));

    switch (args.port)
    {
/*
TAG: portInitRoutine
MODEL{
#if USE_~PORTNAME~ == true 
        case LDRV_~NAME~_PORT_~PORTNAME~:
        
            ~name~->port = ~PORTNAME~_~NAME~_DRIVER_HANDLER;
            ~name~->pvHandler = port_~name~_init_~porname~ (args.~PORTNAME~);

            break;
#endif
}
*/
        
        default:
            assert(false);
            // Unknow device
            break;
    }

    return(~name~);
}


/*
TAG: hdrvPublicFunctions
MODEL{
~returnType~ hdrv_~name~_~fnName~ (hdrv_~name~_h handler, ~argsWithTipes~)
{
    hdrv_~name~_t* this = __get_context(handler); // check and get context
    assert (this->port->~fnName~ != NULL);

    this->port->~fnName~(this->pvHandler ~args~);
}
}
*/