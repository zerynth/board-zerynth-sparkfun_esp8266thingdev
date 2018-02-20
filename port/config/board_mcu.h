#ifndef __BOARD_MCU__
#define __BOARD_MCU__



#define EXT_INTERRUPTS_NEEDED   16



//VHAL Drivers
#define VHAL_GPIO 1
#define VHAL_EXT 1
#define VHAL_SER 1
#define VHAL_NFO 1
#define VHAL_FLASH 1
#define VHAL_RNG 1
/*
#define VHAL_SPI 0
#define VHAL_ADC 0
#define VHAL_I2C 0
#define VHAL_DAC 0
#define VHAL_CAN 0
*/
#define BOARD_HAS_RNG   1




/*Definition of PWM PIN params, for GPIO initialization*/
#define PWM_0_OUT_IO_MUX PERIPHS_IO_MUX_GPIO4_U
#define PWM_0_OUT_IO_NUM 4
#define PWM_0_OUT_IO_FUNC  FUNC_GPIO4

#define PWM_1_OUT_IO_MUX PERIPHS_IO_MUX_MTMS_U
#define PWM_1_OUT_IO_NUM 14
#define PWM_1_OUT_IO_FUNC  FUNC_GPIO14

#define PWM_2_OUT_IO_MUX PERIPHS_IO_MUX_MTDI_U
#define PWM_2_OUT_IO_NUM 12
#define PWM_2_OUT_IO_FUNC  FUNC_GPIO12

#define PWM_3_OUT_IO_MUX PERIPHS_IO_MUX_MTDO_U
#define PWM_3_OUT_IO_NUM 15
#define PWM_3_OUT_IO_FUNC  FUNC_GPIO15

#define PWM_ESP_CHANNELS 4

#endif