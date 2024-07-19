#pragma once

#ifndef __~NAME~_~PORTNAME~_H__
#define __~NAME~_~PORTNAME~_H__

#include <stdint.h>
#include "hDrv_~name~.h"

#define ~NAME~_DRIVER "External ~NAME~: ~PORTNAME~"

// =================================================
// Ldriver defines


extern const ldrv_~name~_port_t *~PORTNAME~_~NAME~_DRIVER_HANDLER; //<! ponteiro para lista de funções do driver, compartilhado para todas as instâncias

// Prototipos de funções
void*       port_~name~_init_~portname~      (~PORTNAME~_init_args_t args);

#endif //__~NAME~_~PORTNAME~_H__