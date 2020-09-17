from django.db import models

# Create your models here.
class Imp(models.Model):
    numero_de_ordem = models.TextField(db_column='NUMERO DE ORDEM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anomes = models.IntegerField(db_column='ANOMES', blank=True, null=True)  # Field name made lowercase.
    cod_ncm = models.IntegerField(db_column='COD.NCM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descricao_do_codigo_ncm = models.TextField(db_column='DESCRICAO DO CODIGO NCM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pais = models.TextField(db_column='PAIS', blank=True, null=True)  # Field name made lowercase.
    pais_de_origem = models.TextField(db_column='PAIS DE ORIGEM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pais_0_field = models.TextField(db_column='PAIS_[0]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pais_de_aquisicao = models.TextField(db_column='PAIS DE AQUISICAO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    und_estat_field = models.IntegerField(db_column='UND.ESTAT.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    unidade_de_medida = models.TextField(db_column='UNIDADE DE MEDIDA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unidade_comerc_field = models.TextField(db_column='UNIDADE COMERC.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    descricao_do_produto = models.TextField(db_column='DESCRICAO DO PRODUTO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qtde_estatistica = models.TextField(db_column='QTDE ESTATISTICA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    peso_liquido = models.TextField(db_column='PESO LIQUIDO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vmle_dolar = models.TextField(db_column='VMLE DOLAR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vl_frete_dolar = models.TextField(db_column='VL FRETE DOLAR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vl_seguro_dolar = models.TextField(db_column='VL SEGURO DOLAR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valor_un_prod_dolar = models.TextField(db_column='VALOR UN.PROD.DOLAR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qtd_comercial_field = models.IntegerField(db_column='QTD COMERCIAL.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tot_un_prod_dolar = models.TextField(db_column='TOT.UN.PROD.DOLAR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unidade_desembarque = models.TextField(db_column='UNIDADE DESEMBARQUE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unidade_desembaraco = models.TextField(db_column='UNIDADE DESEMBARACO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    incoterm = models.TextField(db_column='INCOTERM', blank=True, null=True)  # Field name made lowercase.
    nat_informacao = models.TextField(db_column='NAT.INFORMACAO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    situacao_do_despacho = models.TextField(db_column='SITUACAO DO DESPACHO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __unicode__(self):
        return self.title

    class Meta:
        # managed = False
        db_table = 'imp'