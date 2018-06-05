<?php

if (!defined('FORUM')) die();

// Language definitions used in profile, users, options, moderate, register, groups
$lang_app_post = array(
	'No posts'					=> 'Нет неподтверждённых сообщений в этой теме со времени последнего визита.',
	'Unp posts'					=> 'В виде сообщений',
	'Unp topics'				=> 'В виде тем',
	'Unp users'					=> 'Неподтверждённые регистрации',
	'Title'						=> 'Подтверждение сообщений',
	'Title users'				=> 'Подтверждение регистраций',
	'Approve'					=> 'Подтвердить',
	'Approve reg'				=>'Подтвердить',
	'Remove'					=> 'Удалить',
	'Remove reg'				=> 'Удалить',
	'Sel post'					=> 'Выбрать сообщение',
	'Topics'					=> 'Темы',
	'Topic warning'				=> 'Внимание! Ваше сообщение появится только после подтверждения модератором!!!',
	'warn'						=> 'This is section of unapproved posts.',
	'First topic'				=> 'Topics of this forum are in the process of approving',
	'See posts'					=> 'Посмотреть все неподтверждённые сообщения',
//viewtopic.php
	'time app'					=> 'Сообщение подтверждено модератором %s',
//part features
	'name features part'		=> '<strong>%s.</strong> Post approval',
	'info features'				=> 'Information about this part',
	'text input'				=> 'Allow post approval after ',
	'name check features'		=> 'Show approval date',
	'info check features'		=> 'Enable or daisble show approval date',
	'send email features'		=> 'If there are unapproved posts then send email',
	'everytime'					=> 'Everytime',
	'every hour'				=> 'Every hour',
	'time to day'				=> 'Time to day',
	'time to week'				=> 'Time to week',
//forums.php
	'forum head'				=> 'Edit Post approval settings',
	'forum check'				=> 'Enable posts approval to this forum',
	'forum info'				=> 'This option will allow you to determine whether posts will be aproved or not.',
	'name check'				=> 'Posts approval',
//groups.php
	'legend post approval'				=> 'Post approval',
	'allow without approval'			 => 'Allow posting without approval',
	'allow post approval'				=> 'Allow post approval',
        'allow reg approval'			=>'Allow registration approval',
//users section
	'No results'				=> 'There are no registered users since your last visit.',
	'Check user'				=> '',
	'Approve registration'		=> 'Approve registration',
	'Remove registration'		=> 'Remove registration',
	'Approve all'				=> 'Approve all',
	'Approve success'			=> 'Users approved is successfull and new user is added.',
	'Remove success'			=> 'Users removed is successfull.',
	'Approve not success'		=> 'Approve users is not success.',
	'Remove not success'		=> 'Users removed is not success.',
	'Show unappr regs'				=> 'Unapproved registrations',
//settings -> features
	'users check name'			=> 'Allow registration approval',
	'users check value'			=> 'Enable new registrations approval',
	'rej email name'			=> 'Rejection email',
	'rej email value'			=> 'Don\'t send an email informing user that his registration was rejected' ,
	'admin inf email name'		=> 'Inform admnistrator',
	'admin inf email value'		=> 'Send email to administrator if there are new registrations waiting for approval',
	'option group title'		=> 'Post and registration approval',
	'option confirm removal title'  => 'Post removal confirmation',
	'option confirm removal'        => 'Ask for confirmation when a post waiting for approval is being deleted',
//other page
	'Reg e-mail'				=>'Ваша регистрация должна быть подтверждена администратором. Вы получите об этом e-mail.',
	'registration ip'			=>'IP-адрес регистрации',
	'username'					=>'Логин',
	'email'						=>'E-mail',
	'registered'				=>'Дата регистрации',
	'name page'					=> 'Подтверждение сообщений',
	'no posts'					=> "Со времени вашего последнего визита не появилось неподтверждённых тем.",
	'no topic'					=> 'Нет сообщений',
	'warning'					=> 'Ваше сообщение появится после подтверждения модератором',
	'warning registration'		=>'Ваша регистрация будет завершена после подтверждения администратором.',
	'name 1 col'				=> 'Тема',
	'name 2 col'				=> 'Категория',
	'name 3 col'				=> 'Ответов',
	'name 4 col'				=> 'Последнее сообщение',
	'table summary'				=> 'Темы в форуме %s.',
	'Post topic'				=> 'Создать тему',
	'Views'						=> 'Просмотров',
	'Moved'						=> 'Тема перемещена',
	'Sticky'					=> '[Прикреплено]',
	'Empty forum'				=> '[ Раздел пуст ]',
	'Never'						=> 'Никогда',
	'No topics'					=> 'Нет созданных тем',
	'First topic nag'			=> 'Be the first to post a topic in this forum',
	'Guest post disabled'		=> 'Гостям запрещено создавать темы в этом разделе.',
	'You posted'				=> 'Вы отвечали в этой теме',
	'You posted indicator'		=> '&#183;&#160;',
	'Table summary mods'		=> 'Select which of the listed topics you would like to move, open, close or delete from the forum: ',
	'Permalink forum'			=> 'Постоянная ссылка на этот раздел.',
	'Forum login nag'			=> 'Сообщения для гостей отключены. Вы должны %s или %s, чтобы создать тему.',
	'Moderate forum'			=> 'Moderate forum',
	'Mark forum read'			=> 'Отметить раздел прочитанным',
	'New posts info'			=> 'Идти к первому сообщению со времени последнего визита.',
	'delete sev'				=> 'delete selected posts',
	'delete all'				=> 'delete all posts',
	'delete'					=> 'delete post',
	'app sev'					=> 'approve selected posts',
	'app all'					=> 'approve all posts',
	'approval'					=> 'approve post',
	'delete succesfull'			=> 'The selected posts have been successfully deleted.',
	'approve succesfull'		=> 'The selected posts have been successfully approved.',
	'select post'				=> 'Select post:',
	'topic redirect'			=> 'Post deleted. Redirecting ...',
	'topic red app'				=>	'Post approved. Redirecting ...',
	'show app posts'			=> 'Unapproved posts',
//copyright from lang_topic
	'Topic by'					=> 'Topic by %s:',
	'Reply by'					=> 'Reply by %s:',
	'Post reply'				=> 'Post reply',
	'Topic closed'				=> 'Topic closed',
	'Guest reply disabled'		=> 'Guests may not reply to topics in this forum.',
	'Status'					=> 'Status:',
	'From'						=> 'From:',
	'Registered'				=> 'Registered:',
	'Note'						=> 'Note:',
	'Posts'						=> 'Posts:',
	'IP'						=> 'IP:',
	'Visit website'				=> '<span>%s\'s </span>Website',
	'Guest'						=> 'Guest',
	'Online'					=> 'Online',
	'Offline'					=> 'Offline',
	'Last edited'				=> 'Last edited by %s (%s)',
	'Report'					=> 'Report',
	'Delete'					=> 'Delete',
	'Delete topic'				=> 'Delete topic',
	'Edit'						=> 'Edit',
	'Quote'						=> 'Quote',
	'Cancel subscription'		=> 'Unsubscribe from topic',
	'Subscription'				=> 'Subscribe to topic',
	'Topic login nag'			=> 'Guest posting is disabled. You must %s or %s to post a reply.',
	'Quick post'				=> 'Quick post',
	'Avatar'					=> 'Avatar',
	'Post'						=> 'Post',
	'Cannot delete'				=> 'You cannot delete the first post',
	'Permalink post'			=> 'Permanent link to this post',
	'Permalink topic'			=> 'Permanent link to this topic',
	'Go to profile'				=> 'Go to %s\'s profile',
	'Move'						=> 'Move topic',
	'Open'						=> 'Open topic',
	'Close'						=> 'Close topic',
	'Unstick'					=> 'Unstick topic',
	'Stick'						=> 'Stick topic',
	'Delete posts'				=> 'Delete posts',
	'bann'						=> 'Bann to user',
//errors
	'Badly link argument'		=>	'Ссылка, по которой вы перешли, некорректна.',
	'No db result from posts'	=>	'Нет неподтверждённых сообщений.',
	'Error app topic'			=>	'Error in the table "post_approval_topics". There are no topics. Please reinstall extension.',
	'Post errors'				=>	'Предупреждений:',
//post removal confirmation page
	'Delete topic' => 'Удалить тему',
	'Delete post' => 'Удалить сообщение',
	'Delete topic info'		=>	'Создатель %1$s %2$s.',
	'Topic byline'			=>	'<span>Автор </span>%s',
	'Reply byline'			=>	'<span>Reply by </span>%s',
	'Delete post info'		=>	'Автор %1$s %2$s',
);