using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Language : Element
{
    [JsonProperty("writing"), TextAttribute("")]
    public string writing;
    [JsonProperty("phonology"), TextAttribute("")]
    public string phonology;
    [JsonProperty("grammar"), TextAttribute("")]
    public string grammar;
    [JsonProperty("vocabulary"), TextAttribute("")]
    public string vocabulary;
    [JsonProperty("classification"), ReferenceAttribute(typeof(Construct))]
    public string classification;
    [JsonProperty("prose"), TextAttribute("")]
    public string prose;
    [JsonProperty("speakers"), Integer(0)]
    public int speakers;
    [JsonProperty("dialects"), ReferenceAttribute(typeof(Language), true)]
    public string dialects;
    [JsonProperty("range"), ReferenceAttribute(typeof(Location), true)]
    public string range;
}
