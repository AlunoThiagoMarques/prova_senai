from django.db import models
from tinymce.models import HTMLField
# Create your models here.
# aqui vou vriar minhas classes de entidades
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    biografia = models.TextField()

    def __str__(self):
        return self.nome
    
class EixoTecnologia(models.Model):
      nome = models.CharField(max_length=60)
      def __str__(self):
            return self.nome
      class Meta:
            db_table = 'eixo'

class Artigo(models.Model):
     texto = HTMLField()
     data_publicacao = models.DateTimeField(auto_now_add = True)
     id_fk_eixo = models.ForeignKey(
          EixoTecnologia,
          on_delete=models.CASCADE,
          db_column='id_fk_eixo'
     )
     id_fk_autor = models.ForeignKey(
          Autor,
          on_delete=models.CASCADE,
          db_column='id_fk_autor'
     )

     def __str__(self):
          return f"Artigo {self.id} - {self.data_publicacao}"
     
     class Meta:
          db_table = 'artigo'