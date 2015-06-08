from django.db import models

from materia.models import MateriaLegislativa


class AssuntoNorma(models.Model):
    des_assunto = models.CharField(max_length=50)
    des_estendida = models.CharField(max_length=250, blank=True, null=True)


class TipoNormaJuridica(models.Model):
    voc_lexml = models.CharField(max_length=50, blank=True, null=True)
    sgl_tipo_norma = models.CharField(max_length=3)
    des_tipo_norma = models.CharField(max_length=50)


class NormaJuridica(models.Model):
    tipo = models.ForeignKey(TipoNormaJuridica)
    materia = models.ForeignKey(MateriaLegislativa, blank=True, null=True)
    num_norma = models.IntegerField()
    ano_norma = models.SmallIntegerField()
    tip_esfera_federacao = models.CharField(max_length=1)
    dat_norma = models.DateField(blank=True, null=True)
    dat_publicacao = models.DateField(blank=True, null=True)
    des_veiculo_publicacao = models.CharField(max_length=30, blank=True, null=True)
    num_pag_inicio_publ = models.IntegerField(blank=True, null=True)
    num_pag_fim_publ = models.IntegerField(blank=True, null=True)
    txt_ementa = models.TextField()
    txt_indexacao = models.TextField(blank=True, null=True)
    txt_observacao = models.TextField(blank=True, null=True)
    ind_complemento = models.IntegerField(blank=True, null=True)
    assunto = models.ForeignKey(AssuntoNorma)  # XXX was a CharField (attention on migrate)
    dat_vigencia = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField()


# XXX maybe should be in materia app, but would cause a circular import
class LegislacaoCitada(models.Model):
    materia = models.ForeignKey(MateriaLegislativa)
    norma = models.ForeignKey(NormaJuridica)
    des_disposicoes = models.CharField(max_length=15, blank=True, null=True)
    des_parte = models.CharField(max_length=8, blank=True, null=True)
    des_livro = models.CharField(max_length=7, blank=True, null=True)
    des_titulo = models.CharField(max_length=7, blank=True, null=True)
    des_capitulo = models.CharField(max_length=7, blank=True, null=True)
    des_secao = models.CharField(max_length=7, blank=True, null=True)
    des_subsecao = models.CharField(max_length=7, blank=True, null=True)
    des_artigo = models.CharField(max_length=4, blank=True, null=True)
    des_paragrafo = models.CharField(max_length=3, blank=True, null=True)
    des_inciso = models.CharField(max_length=10, blank=True, null=True)
    des_alinea = models.CharField(max_length=3, blank=True, null=True)
    des_item = models.CharField(max_length=3, blank=True, null=True)


class VinculoNormaJuridica(models.Model):
    norma_referente = models.ForeignKey(NormaJuridica, related_name='+')
    norma_referida = models.ForeignKey(NormaJuridica, related_name='+')
    tip_vinculo = models.CharField(max_length=1, blank=True, null=True)
    ind_excluido = models.CharField(max_length=1)
