#include <avr/io.h>
#include <util/delay.h>

//  PC7 PC6 PC5 PC4 PC3 PC2 PC1 PC0    // PG2  PG1  PG0
//  DB7 DB6 DB5 DB4 DB3 DB2 DB1 DB0    //  E   RW   RS

void COMMAND(unsigned char byte);    // COMMAND 함수 선언
void DATA(unsigned char byte);        // DATA 함수 선언
void init_system(void);                // init_system 함수 선언
void init_LCD(void);                    // init_LCD 함수 선언

int main(void) {

    init_system();
    init_LCD();

    DATA('G');

    while(1);
}

//LCD에 명령을 쓰기 위한 함수

void COMMAND(unsigned char byte)
{
    PORTG = 0xFC;        //PORTG에 RS, RW, E 가 연결되어 있다.
    PORTC = byte;          //PORTC에 데이터버스가 연결되어 있다.
    PORTG ^= 0x04;        //E 신호를 H->L로 하기 위해
    _delay_ms(2);         //LCD 내부 동작시간
}

//LCD에 데이터를 쓰기 위한 함수

void DATA(unsigned char byte)
{
    PORTG = 0xFD;            //PORTG에 RS, RW, E 가 연결되어 있다.
    PORTC = byte;           //PORTC에 데이터버스가 연결되어 있다.
    PORTG ^= 0x04;           //E 신호를 H->L로 하기 위해
    _delay_ms(2);            //LCD 내부 동작시간
}

// ATmega128의 포트 초기화

void init_system(void)
{
     DDRC = 0xFF;              //LCD 데이터 버스
     PORTC = 0xFF;
     DDRG = 0xFF;              //LCD 컨트롤 신호(PG2=LCD_EN, PG1=RW, PG0=RS)
     PORTG = 0xFF;
}

// LCD 초기화

void init_LCD(void)
{
       _delay_ms(15);       //15msec 이상 시간지연
       COMMAND(0x38);         //Function set, 기능셋(데이터버스 8비트, 라인수:2줄)
       _delay_ms(5);        //4.1msec 이상 시간지연, 생략가능
       COMMAND(0x38);         //기능셋, 생략 가능
       _delay_us(100);      //100usec 이상 시간지연, 생략가능
       COMMAND(0x38);          //기능셋, 생략 가능
       COMMAND(0x08);          //표시 Off , 생략 가능
       COMMAND(0x01);       //화면 지우기
       COMMAND(0x06);        //엔트리모드셋
       COMMAND(0x0C);         //표시 on
}
