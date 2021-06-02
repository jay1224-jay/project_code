#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int * sort( int s[3])
{
    int a, b;
    while(!(s[0]<=s[1] & s[1]<=s[2]))
    {
        for(int k = 0;k<2;k++)
        {
            if (s[k]>s[k+1])
            {
                int temp = s[k];
                s[k] = s[k+1];
                s[k+1] = temp;
            }
        }
    }
    return s;
}

int main(){
    
    int n=0, p, t, a=1;
    int list[200][3], p_list[3], clearList[][3]={{}};
    printf("enter perimeter:");
    scanf("%d", &p);
    for(int a=1;a<(p/2)+1;a++) 
    {
        for(int b=1;b<(p/2)+1;b++)
        {
            for(int c=1;c<(p/2)+1;c++)
            {
                if ( a+b+c==p & abs(a-b)<c & abs(c-b)<a & abs(a-c)<b & a+b>c & a+c>b & b+c>a ) 
                {
                    n++;
                    p_list[0] = a;
                    p_list[1] = b;
                    p_list[2] = c;

                    memcpy(p_list, sort(p_list), sizeof(p_list));  //sort(p_list) -> p_list

                    for(int i = 0;i<3;i++) list[n-1][i] = p_list[i];
                }    
            }    
        }    
    }
    printf("==== side ====\n");
    int k=0;
    int g;
    for(int i=0;i<n;i++){
            g=1;
            int a = list[i][0], b = list[i][1], c = list[i][2];
            for(int j=0;j<k;j++){
                if(clearList[j][0]==a & clearList[j][1]==b & clearList[j][2]==c){
                    g=0;
                }
            }
            if(g==1){
                clearList[k][0] = a;
                clearList[k][1] = b;
                clearList[k][2] = c;
                printf("   %-2d %-2d %-2d\n",a,b,c);
                k++;
            }
            
    }
    puts("==============");
    /*
    for (int r=0;r<n;r++){
        printf("in clear %d %d %d \n", clearList[r][0], clearList[r][1], clearList[r][2]);
    }*/
    printf("types: %d\n\n", k);
    system("pause");
    return 0;
}
