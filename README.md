# KARAYEL Takımı Teknofest 2024 Doğal Dil İşleme Yarışması Serbest Kategori

Teknofest 2024 Türkçe Doğal Dil İşleme Yarışması Serbest Kategori'de mücadele eden **KARAYEL** takımı olarak, yeterli akademik danışmanlığa ulaşamayan öğrencilere sunmak üzere bir LLM modeli geliştirmeyi kendimize ana hedef olarak belirledik ve çalışmalarımızı bu doğrultuda gerçekleştirdik.

## Veri Toplama Süreçleri

İlk olarak ve en önemli adım veri seti hazırlamak üzere bir internet sitesi geliştirdik. Geliştirdiğimiz bu internet sitesi aracılığıyla ulaşabildiğimiz ve uzmanlığı bulunan kişilerden öğrencilerin yaşadığı sorunların çözümlerini, öğrencilerden ise yaşamış oldukları problemler ile ilgili veri toplamayı hedefledik. Topladığımız veri seti üzerinde Self-Instruct ve Prompt Engineering yöntemleri başta olmak üzere sentetik veri çoğaltma adımları uygulayarak modelimizde kullandık. Aynı zamanda topladığımız veri setini huggingface platformunda yayınladık.

Geliştirmiş olduğumuz internet sitemizin adresi: https://karayel-web-host.vercel.app/<br>
Geliştirmiş olduğumuz internet sitemizin kaynak kodları: [Karayel-Web-App](https://github.com/karayel-ddi/Karayel-Web-App)
<br><br>
Websitemizin Ana Sayfası:

![Website Ana Sayfa](https://github.com/karayel-ddi/Teknofest_2024_ddi_serbest_kategori/blob/main/media/web-anasayfa.jpg)

Websitemizin Veri Girişi ve Veri Doğrulama Ekranları

<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <img src="https://github.com/karayel-ddi/Teknofest_2024_ddi_serbest_kategori/blob/main/media/web-verigiris.jpg" alt="Web Veri Girişi" style="width:49%; height:200px; object-fit: cover;"/>
  <img src="https://github.com/karayel-ddi/Teknofest_2024_ddi_serbest_kategori/blob/main/media/web-veridogrulama.jpg" alt="Web Veri Doğrulama" style="width:49%; height:200px; object-fit: cover;"/>
</div>
<br><br>  
Modelimizin hedef kitlesinin ihtiyaçlarını düşünerek modelimizin matematik görevlerindeki performansını arttırmak için çalışmalarda bulunduk. Bu doğrultuda huggingface platformunda ingilizce olarak bulunan ve ilgili task için geliştirilen matematik problemleri veri setlerini yayıncılarına atıflarda bulunarak Türkçe'leştirdik. Ardından Türkçe veri setlerini huggingface platformumuzda paylaştık.  <br><br>

[Karayel-DDI/Turkce_Lighteval_MATH-Hard](https://huggingface.co/datasets/Karayel-DDI/Turkce_Lighteval_MATH-Hard)<br>
[Karayel-DDI/Turkce-qwedsacf_grade-school-math-instructions](https://huggingface.co/datasets/Karayel-DDI/Turkce-qwedsacf_grade-school-math-instructions)<br>
[Karayel-DDI/Turkce-hendrycks_competition_math](https://huggingface.co/datasets/Karayel-DDI/Turkce-hendrycks_competition_math)

## Model Eğitimi

Proje kapsamında [LLaMA 3](https://huggingface.co/meta-llama/Meta-Llama-3-8B) modelinin Türkçe kaynak veri setleri ile eğitilmesi sonucu Türkçe dilinde oldukça başarılı performans gösteren [ytu-ce-cosmos/Turkish-Llama-8b-Instruct-v0.1](https://huggingface.co/ytu-ce-cosmos/Turkish-Llama-8b-Instruct-v0.1) modelini fine-tune ettik. Veri toplama süreçleri adımında aktardığımız yöntemlerle edindiğimiz verileri gerekli işlem adımları sonrası modelin instruction-tune görevinde kullandık.<br><br>
Model eğitimi QLORA yakşalımı ile yapılmıştır. Kullanılan eğitim parametreleri ve eğitim kodu github'ta paylaşılmıştır.\
Eğitilen modeli takımımızın [huggingface sayfasında](https://huggingface.co/Karayel-DDI) sayfasında paylaştık. İlgili bağlantıya aşağıdan ulaşabilirsiniz.<br>

[Karayel-DDI/KARAYEL-LLM-q4](https://huggingface.co/Karayel-DDI/KARAYEL-LLM-q4)

## Arayüz Tasarımı

Projemizin 3. adımı olarak geliştirdiğimiz LLM modelini bir chat arayüzü ile sunmak adına geliştirmelerde bulunduk. Bu adımda ki amacımız modelin kullanım senaryolarını arttırmak ve kullanıcıların kolay kullanımına sunmak oldu. Gradio kütüphanesi kullanarak geliştirdiğimiz arayüzümüzün [kaynak kodlarını](https://github.com/karayel-ddi/Teknofest_2024_ddi_serbest_kategori/blob/main/chat.py) github sayfamızda paylaştık. Aşağıda çalışmasını görebilirsiniz.

https://github.com/user-attachments/assets/69fcd5bd-0214-4ae0-bc22-bc5fa47098cc


  
#Acıkhack2024TDDİ  #Türkiye Açık Kaynak Platformu
