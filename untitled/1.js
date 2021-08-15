// 优先自动定位到第一个正在上的课的位置 status=1，没有的话定位到第一个未开课的 status=0
  const scrollLesson = (isRefresh, status) => {
    const hDay = 65 // 一天的额外高度
    const hLesson = 132 // 每节课的行高
    let top = 0 // 初始高度
    let flag = false // 是否找到正在上课的课

    if (!isInit && !isRefresh) {
      return
    }

    for (let i = 0; i < formatLessons.length; i += 1) {
      const lessons = formatLessons[i].children
      let j = 0
      while(j < lessons.length) {
        if (lessons[j].status !== status) {
          j += 1
        } else {
          flag = true
          break
        }
      }
      if (flag) {
        top += (hLesson * (Math.floor((j - 1) / 2)))
        console.log('top add lesson1', Math.floor(j / 2), top)
        break
      } else {
        top += (hLesson * (Math.ceil(j / 2)))
        console.log('top add lesson2', Math.ceil(j / 2), top)
      }
      top += (hDay + 15 * (Math.floor((j + 1) / 2) - 1))
      console.log('top add day', (hDay + 15 * (Math.floor((j + 1) / 2) - 1)))
    }
    if (flag) {
      setIsInit(false)
      autoScroll(top)
    } else if (status === 1) {
      scrollLesson(true, 0)
    }
  }