#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	int i, j, k, l;
	unsigned short *row_in, *row_out;
	char infile[100], outfile[100];
	FILE *fp, *fo;
	int start_index = atoi(argv[2]), end_index = atoi(argv[3]);
	unsigned short* m_frameIn = (unsigned short*)malloc(2*320*240);
	unsigned short* m_frameOut = (unsigned short*)malloc(2*320*240);

	for(k=start_index; k<=end_index; k++) {
		sprintf(infile, "%s%d.yuv", argv[1], k);
		fp = fopen(infile, "r");
		fread(m_frameIn, 2, 320*240, fp);
		fclose(fp);
		sprintf(outfile, "%s%d.pgm", argv[1], k);
		fo = fopen(outfile, "w");
		fprintf(fo, "P2\n320 240\n16383\n");
		for( i = 0; i < 240; ++i )
		{
			row_in = (unsigned short*)m_frameIn + i * 320;
			row_out = m_frameOut + i * 320;
			for( j = 0; j < 320; ++j )
			{
				//row_out[j] = ( row_in[j] << 8 ) | ( row_in[j] >> 8 );
				//row_out[j] = row_out[j] >> 2 ;
				row_out[j] = row_in[j];
			}
		} 

		for(l=0; l < 320*240; l++)
			fprintf(fo, "%d ", m_frameOut[l]);
		fclose(fo);
	}
	free(m_frameIn);
	free(m_frameOut);
}
