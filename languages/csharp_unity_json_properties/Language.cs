using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Language : Element
{
    [JsonProperty("phonology"), TextAttribute("")]
    public string phonology;
    [JsonProperty("grammar"), TextAttribute("")]
    public string grammar;
    [JsonProperty("lexicon"), TextAttribute("")]
    public string lexicon;
    [JsonProperty("writing"), TextAttribute("")]
    public string writing;
    [JsonProperty("classification"), ReferenceAttribute(typeof(Construct))]
    public string classification;
    [JsonProperty("status"), TextAttribute("")]
    public string status;
    [JsonProperty("spread"), ReferenceAttribute(typeof(Location), true)]
    public string spread;
    [JsonProperty("dialects"), ReferenceAttribute(typeof(Language), true)]
    public string dialects;
}
