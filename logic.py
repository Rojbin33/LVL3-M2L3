# Görev 2 - İhtiyacınız olan her şeyi içe aktarın
from discord import ui,ButtonStyle


class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        buttons = []
        for index, option in enumerate(self.options):
            if index == self.__answer_id:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'correct_{index}'))
            else:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'wrong_{index}'))
        # Görev 3 - Dahili klavyeyi oluşturmak için bir metot oluşturun
        return buttons

        
# Görev 4 - Listeyi sorularınızla doldurun
quiz_questions = [
   Question("Kediler onları kimse görmediğinde ne yapar?", 1, "Uyurlar", "Espri yazarlar"),
   Question("Kediler sevgilerini nasıl ifade ederler?", 0, "Yüksek sesle mırıldanırlar", "Sevimli fotoğraflar", "Havlar"),
   Question("Kediler hangi kitapları okumayı sever?", 3, "Kişisel gelişim kitapları", "Zaman yönetimi: Günde 18 saat nasıl uyunur","Sahibinizden 5 dakika erken uyumanın 101 yolu", "İnsan yönetimi rehberi"),
   Question("Kediler lazer ışığını neden bu kadar sever?", 3, "Gizli bir uzaylı teknolojisi olduğunu düşünürler", "Lazerle zamanda yolculuk yaptıklarına inanırlar", "Köpekleri kıskandırmak için", "Avcılık egolarını tatmin etmek için"),
   Question("Kediler neden klavyenin tam üstüne oturur?", 2, "Yazarlık kariyerine başlamak için", "Sıcaklık analizi yaparlar", "İlginizi kontrol ettiklerini sanırlar", "Dosyaları kazara silmek hobileridir"),
   Question("Kediler neden kapalı kapıları açmak ister?", 0, "Orada evrenin sırlarının saklandığını düşünürler", "Sadece 'çünkü olabilir'", "Kapıların özgürlüğüne inanırlar", "Köpekleri etkilemek için")

]

