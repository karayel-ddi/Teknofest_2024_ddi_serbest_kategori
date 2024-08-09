# Teknofest 2024 Doğal Dil İşleme Yarışması Serbest Kategori

Teknofest 2024 Türkçe Doğal Dil İşleme Yarışması Serbest Kategori'de mücadele eden KARAYEL takımı olarak, yeterli akademik danışmanlığa ulaşamayan öğrencilere sunmak üzere bir LLM modeli geliştirmeyi kendimize ana hedef olarak belirledik ve çalışmalarımızı bu doğrultuda gerçekleştirdik.
## Veri Toplama Süreçleri

İlk olarak ve en önemli adım veri seti hazırlamak üzere bir internet sitesi geliştirdik. Geliştirdiğimiz bu internet sitesi aracılığıyla ulaşabildiğimiz ve uzmanlığı bulunan kişilerden öğrencilerin yaşadığı sorunların çözümlerini, öğrencilerden ise yaşamış oldukları problemler ile ilgili veri toplamayı hedefledik. Topladığımız veri seti üzerinde Self-Instruct ve Prompt Engineering yöntemleri başta olmak üzere sentetik veri çoğaltma adımları uygulayarak modelimizde kullandık. Aynı zamanda topladığımız veri setini huggingface platformunda yayınladık.

Geliştirmiş olduğumuz internet sitemizin kaynak kodları: [Karayel-Web-App](https://github.com/karayel-ddi/Karayel-Web-App)

Modelimizin hedef kitlesinin ihtiyaçlarını düşünerek modelimizin matematik görevlerindeki performansını arttırmak için çalışmalarda bulunduk. Bu doğrultuda huggingface platforumnda ingilizce olarak bulunan ve ilgili task için geliştirilen matematik problemleri veri setlerini yayıncılarına atıflarda bulunarak Türkçe'leştirdik. Ardından Türkçe veri setlerini huggingface platformumuzda paylaştık.  
  
[Karayel-DDI/Turkce_Lighteval_MATH-Hard](https://huggingface.co/datasets/Karayel-DDI/Turkce_Lighteval_MATH-Hard)  
[Karayel-DDI/Turkce-qwedsacf_grade-school-math-instructions](https://huggingface.co/datasets/Karayel-DDI/Turkce-qwedsacf_grade-school-math-instructions)  
[Karayel-DDI/Turkce-hendrycks_competition_math](https://huggingface.co/datasets/Karayel-DDI/Turkce-hendrycks_competition_math)
