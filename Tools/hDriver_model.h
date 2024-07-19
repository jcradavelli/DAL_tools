#pragma once

#ifndef __HDRV_~NAME~_H__
#define __HDRV_~NAME~_H__

/*
TAG: subdriverIncludes
MODEL{
#include "hDrv_~subDrvName~.h"
}
*/


typedef void* hdrv_~name~_h;

// Definições de tipos de funções de ~name~
// typedef <tipo de retorno> (*<nome de funcao>) (<args>);
/*
TAG: FunctionTypes
MODEL{
typedef ~returnType~ (*~fnName~_t) (hdrv_~name~_h handler ~argsWithTipes~);
}
*/



// Definições de funções que ddevem ser providas pelo PORT
typedef struct ldrv_~name~_port_
{
/*
TAG: FunctionList
MODEL{
    ~fnName~_t      ~fnName~;
}
*/
}ldrv_~name~_port_t;


// Seleciona o port de ~name~ a ser utilizado
/*
TAG: lDriversUseDefines
MODEL{
#define    USE_~PORTNAME~      (true)
}
*/

// Inclui o arquivo de ~name~ desejado
/*
TAG: lDriversHfiles
MODEL{
#if USE_~PORTNAME~ == true
#include "PORT/~PORTNAME~/lDrv_~name~.h"
#endif
}
*/

// Lista os tipos dde ~name~ disponiveis
typedef enum ldrv_~name~_portList_
{

/*
TAG: lDriversList
MODEL{
#if USE_~PORTNAME~ == true
    LDRV_~NAME~_PORT_~PORTNAME~,
#endif
}
*/

    LDRV_~NAME~_PORT_MAX_VALUE
    
}ldrv_~name~_portlist_t;

typedef struct hdrv_~name~_initArgs_
{
    ldrv_~name~_portlist_t port;
    union{
/*
TAG: lDriverInitArgs
MODEL{
#if USE_~PORTNAME~ == true      
        ~PORTNAME~_init_args_t ~PORTNAME~;
#endif
}
*/
    };
}hdrv_~name~_initArgs_t;

hdrv_~name~_h  hdrv_~name~_init (const hdrv_~name~_initArgs_t ~name~InitArgs);
/*
TAG: hDrvFunctionsPrototypes
MODEL{
~returnType~ hdrv_~name~_~fnName~ (hdrv_~name~_h handler ~argsWithTipes~);
}
*/

#endif //__HDRV_~NAME~_H__