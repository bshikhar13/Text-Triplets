import nltk
nltk.data.path.append('/home/shikhar/Documents/Shikhar/namo/nltk_data')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize , word_tokenize

sample = """
We are also bound by the Buddhist traditions. A famous Korean visitor to India was Hyecho, a Buddhist monk who visited India in the eighth century to know the language and culture of the land of Buddha. He wrote the "account of travel to the five Indian kingdoms". 

We have so much in common. No wonder then that Bollywood films are very popular in Korea. 

Friends! I am here to build upon this relationship. In fact, I have always been fascinated by Korea. I came here when I was Chief Minister of Gujarat and even before that. Honestly speaking, while in Gujarat, I used to wonder as to how a country of the size of Gujarat can do so much economic progress. I ad-mire the spirit of entrepreneurship of the Korean people. I admire the way in which they have created and sustained their global brands. 

From IT and Electronics to Automobile and Steel, Ko-rea has given exemplary products to the world. Similarly, Korean companies are very strong in construction sector and were in-volved in building iconic structures around the world. You also have an impressive infrastructure and record for R & D as well as innovation. 

We in India want to achieve a lot of what Korea has already done. That is why I, along with a large business delega-tion, are here. The good news is that India-Korea bilateral trade has risen after signing of Korea-India CEPA in January 2010. 

The South Korean investment zone in Rajasthan State is progressing well. 

Several Hundred Korean companies are operating in In-dia. Lot of your products particularly in Consumer Electronics are household choices for Indians. And many of them are being pro-duced there. Hyundai Motor is the 2nd largest car manufacturer of India. 

However, there is still a lot of scope for improvement. South Korea ranks only 14th in FDI flows in India. I can admit that the reason for this low volume of FDI lies with us not with you. But I can tell you that India was and is a land of potentials. Now, India is also a land of enabling policy environment. Moreo-ver, there is renewed commitment of my Government for chang-ing the face of the country. We can join hands in the mutual benefit of our people and industry. There is a lot that we can do together. 

For example, there is potential for cooperation between India's software and Korea's hardware industry. Your car making and our designing capabilities can be put together. Though we have become the third biggest producer of steel, we need to add a lot of value in it. Your steel-making capacity and our resources of iron ore can be put together. Your ship-building capacity and our agenda of port led development can become driver of our growth. Infrastructure including housing is another field where we can work together in a big way. 

In my last visit, I had gone to see your wonderful Saemangeum project. We have to create many such Saemangeums. Let us do this for mutual benefit and with a win-win spirit. 

Friends! Since my Government has taken over, we are working day and night to create conditions for faster and inclusive growth. We want a quantum jump in all this. There is no time for incremental changes. The sectors which are strong in Korea are very important for the development of my country. Many of you are already present in India. For those who are not there, I extend an invitation to come to India and explore the opportunities. 

With your presence in India and through your interac-tions with our CEOs, you must already be knowing what we are doing and in which direction we are going. I would only throw some light on the size and scale of the opportunities.   

Water, Transportation, Railways, Sea ports, ship-building, Electricity including renewable, IT infrastructure and services, Electronics, Construction Industry, are all very promis-ing sectors in my country. 

Just to give you some examples: we have planned to build 50 million houses by 2022. In addition, we are going to de-velop smart cities, long industrial corridors, and mega investment regions. For this purpose, we have refined our FDI Policy in con-struction. We have eased the conditions for Real Estate Invest-ment Trusts for making investments. We are also coming up with a regulatory framework for this sector. 

We have targeted 175 Giga Watt of renewable energy in next few years. In addition to generation, the issues of transmission and distribution of electricity are equally important for us. 

We are keen to modernize our Railways, We are plan-ning metro rail in fifty cities and high speed trains in various cor-ridors. We have to upgrade our Highways. 

This year we have made maximum allocation for these two sectors. In addition we have opened up Railways for 100% FDI. 

We are putting up new ports and modernizing the old ones through an ambitious plan called Sagarmala. There is a similar focus on upgrading the existing Airports and putting up regional airports to enhance connectivity to places of economic and tourist importance. 

We particularly want to promote manufacturing in a big way to create jobs for our youth. For this purpose, we have launched a campaign called “Make in India”. This campaign and commitment includes bringing our industrial infrastructure, policies and practices to best global standards and to convert India into a global manufacturing hub. To provide digital infrastructure across the country, we have launched another campaign called Digital India. 

Cleaner and greener development and Zero defect Zero effect manufacturing is another commitment. We have launched a clean India campaign with emphasis on adoption of better environmental technologies.

To enable all this, in last eleven months, we have taken a series of measures to improve the business environment and en-hance the investor confidence. We do believe that ‘ease of doing Business’ has become an important factor in attracting invest-ments in the country. We also believe that FDI is important and it will not come in the country without a globally competitive busi-ness environment. So, we are working aggressively for making India a very easy place to do business. 

To create employment and self-employment opportuni-ties in the country, we have launched the Skill India Missionand other innovative missions. On the other hand, we have fast tracked approvals in industry and infrastructure. This includes en-vironmental clearances, industrial and shipping licences. In addi-tion, we also enhanced the FDI limits in key sectors like Defence and Insurance. We also refined the FDI policy in medical devices sector to encourage the manufacturing of medical equipment. 

Within a very short time, we introduced GST Bill in parliament. We are making our taxation system more stable, pre-dictable and transparent. We have already resolved many taxation issues affecting the foreign investors. This is all to become more conducive for business and bring in technology and capital. 

We have got good results of these initial steps. The sen-timents for private investment and inflow of foreign investment are positive. Our growth rate is above 7%. FDI inflows have gone up by 39% during April-2014 and February-2015 against the same period in previous year. 

Many international financial institutions including the World Bank, IMF, OECD and others are predicting even faster growth in the coming years. MOODY’s have recently upgraded the rating of India as positive on account of our concrete steps in various economic segments. 

Thus, we have restored the global positioning of India in terms of its politics, governance and economy. But we are not going to stop here. We have to and we will do a lot better. 

Friends! once again, I invite you to India to see the change. We are also prepared to work with you in making the conditions more conducive for you. 

Yesterday, I announced the forming of a dedicated me-chanism for hand holding of Korean investors. It will be known as Korea Plus. In addition I assure you of my personal attention if there are any issues. 

Thank you.
"""

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(sample)

filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []

for w in word_tokens :
    if w not in stop_words :
        filtered_sentence.append(w)


print(word_tokens)
print(filtered_sentence)
