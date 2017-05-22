var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', () => {
  gulp.src('music/static/music/scss/**/*.scss')
    .pipe(sass())
    .on('error', (err) => {
      console.log(err.toString());

      this.emit('end');
    })
    .pipe(gulp.dest('music/static/music/css'));
});


gulp.task('watch', () => {  
  gulp.watch('music/static/music/scss/**/*.scss', ['sass']);
})


gulp.task('default', ['sass', 'watch']);