from django.forms import ModelForm

from .models import Movie, CastMember, CastMemberComment


class CastMemberForm(ModelForm):
    class Meta:
        model = CastMember
        fields = ("name", 
                  "born", 
                  "member_slug",
        )


class CastMemberCommentForm(ModelForm):
    class Meta:
        model = CastMemberComment
        fields = ("cast_member", 
                  "movie", 
                  "comment",
        )


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ("title", 
                  "year", 
                  "grade", 
                  "watched", 
                  "comments", 
                  "cast",
                  "genres",
                  "is_top", 
                  "is_sound", 
                  "sound_comments", 
                  "is_beauty", 
                  "beauty_comments", 
                  "is_adult", 
                  "adult_comments", 
                  "is_rewatch", 
                  "rewatch_comments", 
                  "movie_slug",
        )