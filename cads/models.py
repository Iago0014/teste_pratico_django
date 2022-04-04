from django.db import models


# Create your models here.

# função de criação da tabela.
class Cliente(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=25)
    idade = models.IntegerField()
    data_nasc = models.DateField()
    email_cliente = models.CharField(max_length=100)
    apelido = models.CharField(max_length=15)
    observacao = models.CharField(max_length=255)


    class Meta:
        db_table = 'cliente'

    def get_data_nasc(self):
        return self.data_nasc.strftime('%d/%m/%Y')

    def get_input_data_nasc(self):
        return self.data_nasc.strftime('%d/%m/%Y')



    

