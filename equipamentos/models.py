from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    UNIDADE = 'UN'
    METRO = 'M'
    KIT = 'KIT'

    UNIDADES_MEDIDA = [
        (UNIDADE, 'Unidade'),
        (METRO, 'Metro'),
        (KIT, 'Kit'),
    ]

    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    unidade_medida = models.CharField(
        max_length=10,
        choices=UNIDADES_MEDIDA,
        default=UNIDADE
    )
    imagem = models.ImageField(
        upload_to='equipamentos/',
        blank=True,
        null=True
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='equipamentos'
    )
    atividades = models.ManyToManyField(
        'Atividade',
        related_name='equipamentos',
        blank=True
    )

    def __str__(self):
        return self.nome


class Kit(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(
        upload_to='kits/',
        blank=True,
        null=True
    )
    equipamentos = models.ManyToManyField(
        Equipamento,
        through='ItemKit',
        related_name='kits',
        blank=True
    )

    def __str__(self):
        return self.nome


class ItemKit(models.Model):
    kit = models.ForeignKey(
        Kit,
        on_delete=models.CASCADE,
        related_name='itens'
    )
    equipamento = models.ForeignKey(
        Equipamento,
        on_delete=models.CASCADE,
        related_name='itens_kit'
    )
    quantidade = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['kit', 'equipamento'],
                name='unique_kit_equipamento'
            )
        ]

    def __str__(self):
        return f'{self.kit.nome} - {self.equipamento.nome}'


class Atividade(models.Model):
    titulo = models.CharField(max_length=200)
    objetivo = models.TextField()
    descricao = models.TextField(blank=True)
    organizacao = models.CharField(max_length=200, blank=True)
    produto_esperado = models.TextField(blank=True)
    kit = models.ForeignKey(
        Kit,
        on_delete=models.CASCADE,
        related_name='atividades'
    )

    def __str__(self):
        return self.titulo


class Etapa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ordem = models.PositiveIntegerField(default=1)
    imagem = models.ImageField(
        upload_to='etapas/',
        blank=True,
        null=True
    )
    atividade = models.ForeignKey(
        Atividade,
        on_delete=models.CASCADE,
        related_name='etapas'
    )

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f'{self.atividade.titulo} - {self.titulo}'