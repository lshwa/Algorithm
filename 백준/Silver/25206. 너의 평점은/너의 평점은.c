#include <stdio.h>
#include <string.h>

typedef struct 
{
    char name[50];
    float credit;
    char grade[2];
} Student;

int main(void)
{
    Student arr[20];
    double total_score = 0.0;
    double credit_score = 0.0;

    for(int i = 0; i < 20; i++)
    {
        scanf("%s", arr[i].name);
        scanf("%f", &arr[i].credit);
        scanf("%s", arr[i].grade);
        if (strcmp(arr[i].grade, "A+") == 0)
        {
            total_score += arr[i].credit * 4.5;
            credit_score += arr[i].credit;
        }
        else if (strcmp(arr[i].grade, "A0") == 0)
        {
            total_score += arr[i].credit * 4.0;
            credit_score += arr[i].credit;
        }
        else if (strcmp(arr[i].grade, "B+") == 0)
        {
            total_score += arr[i].credit * 3.5;
            credit_score += arr[i].credit;
        }
        else if (strcmp(arr[i].grade, "B0") == 0)
        {
            total_score += arr[i].credit * 3.0;
            credit_score += arr[i].credit;
        }
        else if (strcmp(arr[i].grade, "C+") == 0)
        {
            total_score += arr[i].credit * 2.5; 
            credit_score += arr[i].credit;
        }
        else if (strcmp(arr[i].grade, "C0") == 0)
        {
            total_score += arr[i].credit * 2.0;
            credit_score += arr[i].credit;
        }
        else if (strcmp(arr[i].grade, "D+") == 0)
        {
            total_score += arr[i].credit * 1.5;
            credit_score += arr[i].credit;
        }
        else if (strcmp(arr[i].grade, "D0") == 0)
        {
            total_score += arr[i].credit * 1.0;
            credit_score += arr[i].credit;
        }
        else if (strcmp(arr[i].grade, "F") == 0)
        {
            total_score += arr[i].credit * 0.0;
            credit_score += arr[i].credit;
        }
        else continue;
    }

    printf("%f\n", total_score / credit_score);
    return 0;
}