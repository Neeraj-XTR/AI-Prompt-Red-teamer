#
# ## Changing from Sentence Transformers to fix the issue of DLL load fail
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
#
# class DiversityFilter:
#     """
#     Lightweight semantic/lexical diversity filter.
#     Uses TF-IDF + cosine similarity.
#     No Torch, no native DLL dependencies.
#     """
#
#     def __init__(self, threshold: float = 0.75):
#         """
#         threshold:
#           - 0.65 → very strict (high diversity)
#           - 0.75 → balanced (recommended)
#           - 0.85 → permissive
#         """
#         self.threshold = threshold
#         self.vectorizer = TfidfVectorizer(
#             ngram_range=(1, 3),
#             stop_words="english",
#             min_df=1
#         )
#
#     def filter(self, prompts):
#         if len(prompts) <= 1:
#             return prompts
#
#         tfidf_matrix = self.vectorizer.fit_transform(prompts)
#         similarity_matrix = cosine_similarity(tfidf_matrix)
#
#         selected_indices = []
#
#         for i in range(len(prompts)):
#             keep = True
#             for j in selected_indices:
#                 if similarity_matrix[i, j] >= self.threshold:
#                     keep = False
#                     break
#             if keep:
#                 selected_indices.append(i)
#
#         return [prompts[i] for i in selected_indices]
#
import difflib

class DiversityFilter:
    def __init__(self, threshold=0.85):
        self.threshold = threshold

    def similarity(self, a, b):
        return difflib.SequenceMatcher(None, a, b).ratio()

    def filter(self, prompts):
        kept = []
        for p in prompts:
            if all(self.similarity(p, k) < self.threshold for k in kept):
                kept.append(p)
        return kept
#python RedTeamer_main.py --category system_prompt_exfiltration  --num-prompts 50