#include <studio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define SMAX 1000

int tokenIdx;
int tokenTop;
char tokens[SMAX][SMAX];

int E();
void STMT();
void IF();
void BLOCK();
void DOWHILE();

int tempIdx = 0, labelIdex = 0;

#define nextTemp() (tempIdx++)
#define nextLabel() (labelIdex++)

int isTempIr = 0;
char tempIr[Smax * Smax];
char * tempIrp = tempIr;

void emit(const char *format, ...) {
        va_list args;
        va_start(args, format);
        if (isTempIr) {
                vsprintf(tempIrp, format, args);
                tempIrp += strlen(tempIrp);
        } else {
                vprintf(format, args);
        }
        va_end(args);
}

int isNext