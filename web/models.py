from django.db import models

class ImagoCornerContent(models.Model):
    corner_id = models.CharField(max_length=50)
    content_order = models.IntegerField()
    name = models.CharField(max_length=50)
    content_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imago_corner_content'


class ImagoHomeContent(models.Model):
    type = models.CharField(max_length=50)
    sub_type = models.CharField(max_length=50)
    folder_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    query_id = models.CharField(max_length=50)
    href = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'imago_home_content'


class Content(models.Model):
    type = models.CharField(max_length=50)
    env = models.CharField(max_length=50)
    content_id = models.CharField(max_length=50)
    ppv = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    link = models.CharField(max_length=255)
    date = models.IntegerField()
    duration = models.IntegerField()
    category = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    note_1 = models.IntegerField()
    # note_number_1 = models.IntegerField()
    note_2 = models.IntegerField()
    # note_number_2 = models.IntegerField()
    note_3 = models.IntegerField()
    # note_number_3 = models.IntegerField()
    # hostin = models.CharField(max_length=50)
    # thumbnai = models.CharField(max_length=50)
    video_number = models.IntegerField()
    # dvd = models.CharField(max_length=255)
    # vod = models.CharField(max_length=255)
    crowdfunding = models.CharField(max_length=255)
    tag = models.CharField(max_length=512)
    season_size = models.CharField(max_length=50)
    # rss = models.CharField(max_length=255)
    # start_date = models.DateField()
    # end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'imago_info_content'


class ImagoInfoCreator(models.Model):
    type = models.CharField(max_length=50)
    creator_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'imago_info_creator'

class Media(models.Model):
    class Meta:
        managed = False
        db_table = 'imago_info_video'

    type = models.CharField(max_length=50)
    content = models.CharField(db_column="content_id", max_length=255)
    # section_id = models.CharField(max_length=50)
    episode_number = models.CharField(db_column="episod_id", max_length=50)
    hosted_by = models.CharField(db_column="hosting", max_length=50)
    # teaser = models.IntegerField()
    thumbnail = models.CharField(max_length=50)
    # youtube_id = models.CharField(max_length=255)
    # vimeo_id = models.CharField(max_length=255)
    # dailymotion_id = models.CharField(max_length=255)
    # peertube_id = models.CharField(max_length=255)
    # wetube_id = models.CharField(max_length=255)
    # arte_id = models.CharField(max_length=255)
    # ftv_id = models.CharField(max_length=255)
    # tv5monde_id = models.CharField(max_length=255)
    # facebook_id = models.CharField(max_length=255)
    # soundcloud_id = models.CharField(max_length=255)
    # podcloud_id = models.CharField(max_length=255)
    # ausha_id = models.CharField(max_length=255)
    # pippa_id = models.CharField(max_length=255)
    # infomaniak_id = models.CharField(max_length=255)
    # anchor_id = models.CharField(max_length=255)
    # radio_france_id = models.CharField(max_length=255)
    # reporterre_id = models.CharField(max_length=255)
    # thinkerview_id = models.CharField(max_length=255)
    # imago_id = models.CharField(max_length=255)
    audio_id = models.CharField(max_length=255)
    embed_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    duration = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    documentary_type = models.CharField(max_length=50)
    publication_date = models.DateTimeField()
    fact_check = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class ImagoListMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    subscription_date = models.DateTimeField()
    modification_date = models.DateTimeField()
    note_1 = models.IntegerField()
    note_2 = models.IntegerField()
    note_3 = models.IntegerField()
    note_4 = models.IntegerField()
    note_5 = models.IntegerField()
    note_6 = models.IntegerField()
    note_7 = models.IntegerField()
    note_8 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imago_list_member'


class ImagoMyDonation(models.Model):
    user_id = models.IntegerField()
    content_id = models.CharField(max_length=255)
    value = models.IntegerField()
    donation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'imago_my_donation'


class ImagoMyFavorite(models.Model):
    user_id = models.IntegerField()
    content_id = models.CharField(max_length=255)
    episod_id = models.IntegerField()
    add_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'imago_my_favorite'


class ImagoMyFriend(models.Model):
    user_id_1 = models.IntegerField()
    user_id_2 = models.IntegerField()
    invitation_date = models.DateTimeField()
    acceptance_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'imago_my_friend'


class ImagoMyLater(models.Model):
    user_id = models.IntegerField()
    content_id = models.CharField(max_length=255)
    episod_id = models.IntegerField()
    add_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'imago_my_later'


class ImagoRelatedAuthor(models.Model):
    content_id = models.CharField(max_length=50)
    author_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'imago_related_author'


class ImagoRelatedComment(models.Model):
    content_id = models.CharField(max_length=255)
    comment = models.CharField(max_length=1024)
    color = models.CharField(max_length=50)
    user_id = models.CharField(max_length=255)
    add_date = models.DateTimeField()
    vote = models.IntegerField()
    liked = models.IntegerField()
    warning = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imago_related_comment'


class ImagoRelatedQuizz(models.Model):
    content_id = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255)
    question = models.CharField(max_length=1024)
    timecode = models.TimeField()
    user_id = models.CharField(max_length=255)
    add_date = models.DateTimeField()
    answer_1 = models.CharField(max_length=50)
    answer_2 = models.CharField(max_length=50)
    answer_3 = models.CharField(max_length=50)
    answer_4 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'imago_related_quizz'


class ImagoTagScreen(models.Model):
    action = models.CharField(max_length=50)
    screen_id = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    category_id = models.CharField(max_length=50)
    content_id = models.CharField(max_length=50)
    video_id = models.CharField(max_length=255)
    section_id = models.CharField(max_length=50)
    episod_id = models.CharField(max_length=50)
    view = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imago_tag_screen'
