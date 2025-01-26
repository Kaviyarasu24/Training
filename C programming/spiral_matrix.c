#include<stdio.h>
int y,guj1=0,guj2=0;

void check()
{
	if(guj2 == y)
	{
		guj2=0;
		guj1++;
	}
}
int main()
{
scanf("%d",&y);
	int k1[y][y],k2[y][y];
	int i,j,rl=0,ru=y-1,cl=0,cu=y-1;
	for(i=0;i<y;i++)
		{
			for(j=0;j<y;j++)
				{
					scanf("%d",&k1[i][j]);
				}
		}
	while(rl<= ru && cl <= cu)
		{
			for(i=cl;i<=cu;i++)
				{
					k2[rl][i]=k1[guj1][guj2];
					guj2++;
					check();
					
				}
			rl++;
			for(i=rl;i<=ru;i++)
				{
					k2[i][cu]=k1[guj1][guj2];
					guj2++;
					check();
				}
			cu--;
			if((rl > ru) || (cl>cu))
			break;
			for(i=cu;i>=cl;i--)
				{
					k2[ru][i]=k1[guj1][guj2];
					guj2++;
					check();
				}
			ru--;
			for(i=ru;i>=rl;i--)
				{
					k2[i][cl]=k1[guj1][guj2];
					guj2++;
					check();
				}
			cl++;
		}
