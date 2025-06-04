using System;
using System.Collections.Generic;
[System.Serializable]
public class Language : BaseElement
{
    // Syntax
    public string Writing;
    public string Phonology;
    public string Grammar;
    public string Vocabulary;
    public string ClassificationId;
    // Spread
    public string Prose;
    public int? Speakers;
    public List<string> DialectsIds; = new List<string>();
    public List<string> RangeIds; = new List<string>();
}
