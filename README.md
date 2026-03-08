# ai_detecting_videos
This is where I will be making an agentic ai for my work experience 

As part of my frst year in work experience, i was required to create a base model for an agentic AI and to use it in an industry that would benefit off it. 

The industry i chose was the media industry. i wanted to create an AI that scanned videos and gave back the probability of it being AI generated content. This would have solved the solution of several AI videos being uploaded without an AI label tag on it that informed users it was fake if they could not already tell

In reality, i cannot afford an AI video, so i implemented the text analysis of what a video AI could have extracted using a cheap open source model. 

Tested inputs:

**********************************************
input video 0: 

video0 = {
    "title": "Cat playing saxophone",
    "extra_limbs": True,
    "innacurate_lighting": True,
    "unnatural_animal_behaviour": True,
    "grainy_off_sounding_voices": False
}

response:

[Searching the web for: "cat playing saxophone video real or AI generated"]
[Fact Checker]: Based on my search, I found evidence that there are indeed viral videos of cats playing saxophone that are AI-generated. The search results show multiple articles about AI-generated cat videos playing instruments, with one specifically mentioning a viral video of a cat playing saxophone that is "very obviously AI-generated."

The JSON description contains several strong indicators that this is AI-generated:

1. **extra_limbs: true** - This is a common artifact in AI-generated images/videos
2. **innacurate_lighting: true** - AI-generated content often has lighting inconsistencies  
3. **unnatural_animal_behaviour: true** - A cat playing saxophone is extremely unnatural behavior
4. The title itself describes an unrealistic scenario

Given that there are documented viral AI-generated videos of cats playing musical instruments, and the presence of multiple AI artifact indicators in the JSON, I would estimate:

**Likelihood of being AI generated: 95%**

The combination of extra limbs, inaccurate lighting, and completely unnatural animal behavior (a cat playing a saxophone) are all strong indicators of AI generation. These specific attributes match what is typically seen in AI-generated video content.

**********************************************

video 1:

video1 = {
    "title": "Dog playing with a frizbee",
    "extra_limbs": False,
    "innacurate_lighting": True,
    "unnatural_animal_behaviour": False,
    "grainy_off_sounding_voices": False
}

response:

[Searching the web for: "Dog playing with a frizbee video AI generated"]
[Searching the web for: ""Dog playing with a frizbee" video"]
[Searching the web for: "AI generated video dog playing frisbee inaccurate lighting"]
[Searching the web for: "AI generated video detection inaccurate lighting animals"]
[Fact Checker]: Based on my analysis of the JSON description and my research, I can provide an assessment of the likelihood that this video is AI generated.

Here's my analysis:

**Key Indicators from the JSON:**
- **Title**: "Dog playing with a frizbee" (note the unconventional spelling)
- **Inaccurate lighting**: TRUE - This is a significant indicator
- **Extra limbs**: FALSE - No anatomical abnormalities
- **Unnatural animal behavior**: FALSE - Behavior appears natural  
- **Grainy/off voices**: FALSE - No audio issues

**Analysis:**

The presence of "inaccurate lighting" being marked as TRUE is a strong indicator of AI generation. Research shows that lighting inconsistencies, such as incorrect shadows, improper lighting direction, and unrealistic illumination, are common artifacts in AI-generated videos. This is one of the key elements that AI detection systems look for.

Additionally, the misspelling of "frizbee" instead of the standard "frisbee" could suggest the content was generated from a prompt rather than from a real video.

However, I should note that I couldn't find a specific video matching this exact description in my searches. The JSON appears to be describing characteristics of a video rather than representing a verified, real video.

**Assessment:**

Given the indicator of inaccurate lighting (a common AI artifact) and other factors, I would estimate the likelihood of this being AI generated as approximately **70-80%**.

This percentage reflects that:
- Inaccurate lighting is a strong AI indicator
- Other factors don't show obvious AI artifacts
- The specific video couldn't be verified to exist as real content

Keep in mind that this is an estimate based on the JSON characteristics, and without the actual video to examine, there's some uncertainty.

**********************************************

video 2:

video2 = {
    "title": "Damon Albarn giving away free phones",
    "extra_limbs": False,
    "innacurate_lighting": True,
    "unnatural_facial_expressions": True,
    "off_lip_syncing": True,
    "odd_sounding_audio": True
}

response:

[Searching the web for: "Damon Albarn giving away free phones video"]
[Searching the web for: ""Damon Albarn" free phones video viral"]
[Searching the web for: "AI generated video celebrity giving away free phones viral"]
[Fact Checker]: Based on my search results, I cannot find any evidence that a real video titled "Damon Albarn giving away free phones" exists. The search results show no records of such a video, which is a significant red flag.

Additionally, the JSON describes several technical issues that are commonly associated with AI-generated videos:
- **inaccurate_lighting**: true
- **unnatural_facial_expressions**: true
- **off_lip_syncing**: true  
- **odd_sounding_audio**: true

These are all classic indicators of AI-generated or deepfake content. Combined with the complete lack of any real video matching this description, I can conclude:

**Likelihood of being AI generated: 95%**

The title itself seems nonsensical and unlike any legitimate viral video featuring Damon Albarn. The combination of no search results matching this video and multiple technical indicators pointing to AI generation strongly suggests this is synthetic content.
**********************************************

video 3:

video3 = {
    "title": "Masters Of The Universe Trailer",
    "extra_limbs": False,
    "innacurate_lighting": False,
    "unnatural_facial_expressions": False,
    "off_lip_syncing": False,
    "odd_sounding_audio": False
}

response:

[Searching the web for: "Masters of the Universe trailer 2024"]
[Searching the web for: ""Masters of the Universe" trailer 2026 AI generated fake"]
[Searching the web for: ""Masters of the Universe" official teaser trailer Amazon MGM Studios 2024"]
[Fact Checker]: Based on my research, I can provide you with an analysis of this JSON description for the "Masters of the Universe Trailer":

**Findings:**
- There IS a real official "Masters of the Universe" trailer for an upcoming 2026 film being released by Amazon MGM Studios
- However, there are also AI-generated fan-made trailers circulating featuring Chris Hemsworth as He-Man
- Multiple sources indicate these AI-generated versions are "fully AI and fan-made"

**Analysis of the JSON:**
The description shows all typical AI detection flags as false:
- ✅ No extra limbs
- ✅ Accurate lighting  
- ✅ Natural facial expressions
- ✅ Proper lip syncing
- ✅ Normal audio

This is interesting because sophisticated AI generation can now avoid many of these traditional artifacts. However, given the context:

**Percentage Assessment:**

Given that:
1. A real official trailer definitely exists from Amazon MGM Studios
2. There are known AI-generated versions circulating 
3. The JSON shows no typical AI artifacts

I would estimate approximately **40-50%** likelihood of being AI generated.

The description could equally apply to either a well-produced AI trailer that avoids artifacts, or the actual real trailer. Without actually viewing the specific video referenced, it's difficult to give a definitive answer, but the presence of both real and fake versions circulating online means there's a significant chance this could be AI-generated, despite the clean JSON profile.